import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from datetime import datetime
import json

from saludtechalpes.config.db import db
from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.comandos import ComandoObtenerImagen, ComandoRollbackExportarImagen
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando
from saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes
from saludtechalpes.modulos.imagenes.aplicacion.comandos.eliminar_registros_exportados import EliminarRegistrosExportados
from saludtechalpes.seedwork.infraestructura import utils
from saludtechalpes.api import app
from saludtechalpes.modulos.imagenes.aplicacion.mapeadores import MapeadorImagenDTOJson
from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.eventos import EventoExportacionImagenesFinalizado, EventoExportacionImagenesFinalizadoPayload, EventoDatosAnonimizados, EventoDatosAnonimizadosPayload
from saludtechalpes.modulos.imagenes.infraestructura.despachadores import Despachador
from saludtechalpes.modulos.imagenes.infraestructura.dto import ImagenesExportadas

def suscribirse_a_comandos():
    cliente= None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-obtener-imagenes', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtech-sub-comandos', schema=AvroSchema(ComandoObtenerImagen))
        while True:   

            mensaje = consumidor.receive()
            comando_integracion = mensaje.value().data
            print(f'Comando recibido: {mensaje.value().data}')

            comando = ObtenerImagenes(
                tipo_imagen= comando_integracion.tipo_imagen,
                tipo_patologia= comando_integracion.tipo_patologia
            )
            with app.app_context():
                resultado_imagenes = ejecutar_query(comando)
                map_imagen = MapeadorImagenDTOJson()
                imagen = [map_imagen.dto_a_externo(resultado) for resultado in resultado_imagenes.resultado]

                imagenes_exportadas = ImagenesExportadas(
                    id = comando_integracion.id,
                    total_imagenes = len(imagen),
                    imagenes=json.dumps(imagen, default=handle_json_serialization)
                )
                db.session.add(imagenes_exportadas)
                db.session.commit()

                eventoFinalizado = EventoExportacionImagenesFinalizado(
                    data = EventoExportacionImagenesFinalizadoPayload(
                        id = comando_integracion.id,
                        mensaje = "La exportacion de imagenes ha sido exitosa",
                        cantidad_imagenes_exportadas = len(imagen),
                        estado = "Exitoso",
                        timestamp = int(datetime.now().timestamp())
                    )
                )
                despachador = Despachador()
                despachador.publicar_evento(eventoFinalizado, 'eventos-notificaciones')

                evento_datos_anonimizados = EventoDatosAnonimizados(
                    data = EventoDatosAnonimizadosPayload(
                        id = comando_integracion.id,
                        estado = 'Exitoso'
                    )
                )
                despachador.publicar_evento(evento_datos_anonimizados, 'eventos-datos-anonimizados')

            consumidor.acknowledge(mensaje)   

            
        cliente.close()
    except: 
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_rollback():
    cliente= None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('revertir-obtencion-imagenes', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='rollback-subscription', schema=AvroSchema(ComandoRollbackExportarImagen))
        while True:
            mensaje = consumidor.receive()
            comando_integracion = mensaje.value().data
            print(f'Comando recibido: {mensaje.value().data}')

            comando = EliminarRegistrosExportados(
                id = comando_integracion.id
            )

            with app.app_context():
                ejecutar_commando(comando)
                evento_datos_anonimizados = EventoDatosAnonimizados(
                    data = EventoDatosAnonimizadosPayload(
                        id = comando_integracion.id,
                        estado = 'Exitoso'
                    )
                )
                despachador = Despachador()
                despachador.publicar_evento(evento_datos_anonimizados, 'eventos-datos-anonimizados')

            consumidor.acknowledge(mensaje)
        cliente.close()
    except: 
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
            

def suscribirse_a_eventos():
    raise NotImplementedError

def handle_json_serialization(obj):
    # Handle UUID objects
    if isinstance(obj, uuid.UUID):
        return str(obj)
    # Handle datetime objects
    elif isinstance(obj, datetime):
        return obj.isoformat()  # Convert to ISO 8601 string
    # Add handling for other types here if needed
    else:
        # Print debug information about the unsupported type
        print(f"Non-serializable object: {obj} ({type(obj)})")
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")