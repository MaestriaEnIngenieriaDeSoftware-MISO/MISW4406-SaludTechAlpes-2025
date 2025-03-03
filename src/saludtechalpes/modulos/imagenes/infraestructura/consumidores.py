import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.comandos import ComandoObtenerImagen
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
from saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes
from saludtechalpes.seedwork.infraestructura import utils
from saludtechalpes.api import app
from saludtechalpes.modulos.imagenes.aplicacion.mapeadores import MapeadorImagenDTOJson
from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.eventos import EventoExportacionImagenesFinalizado, EventoExportacionImagenesFinalizadoPayload
from saludtechalpes.modulos.imagenes.infraestructura.despachadores import Despachador

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

                eventoFinalizado = EventoExportacionImagenesFinalizado(
                    data = EventoExportacionImagenesFinalizadoPayload(
                        mensaje = "La exportacion de imagenes ha sido exitosa",
                        cantidad_imagenes_exportadas = len(imagen),
                        estado = "Exitoso",
                        timestamp = int(datetime.datetime.now().timestamp())
                    )
                )
                despachador = Despachador()
                despachador.publicar_evento(eventoFinalizado, 'eventos-notificaciones')

            consumidor.acknowledge(mensaje)   

            
        cliente.close()
    except: 
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos():
    raise NotImplementedError