import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.comandos import ComandoObtenerImagen
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
from saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes
from saludtechalpes.seedwork.infraestructura import utils
from saludtechalpes.api import app
from saludtechalpes.modulos.imagenes.aplicacion.mapeadores import MapeadorImagenDTOJson


def suscribirse_a_comandos():
    cliente= None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-obtener-imagenes', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='saludtech-sub-comandos', schema=AvroSchema(ComandoObtenerImagen))
        while True:
            mensaje = consumidor.receive()
            comando_integracion = mensaje.value().data
            print(f'Comando recibido: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)   

            comando = ObtenerImagenes(
                id= 1
            )
            with app.app_context():
                resultado = ejecutar_query(comando)
                print('LO LOGREEEEEEEEEE')
                map_imagen = MapeadorImagenDTOJson()
                imagen = map_imagen.dto_a_externo(resultado.resultado)
                print(imagen)
            #consumidor.acknowledge(mensaje)   

            
        cliente.close()
    except: 
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos():
    raise NotImplementedError