import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import datetime

from exportacionsta.modulos.exportacion.infraestructura.schema.v1.comandos import NotificacionEventoEstado, ComandoRollbackExportarImagen, ComandoRollbackExportarImagenPayload
from exportacionsta.seedwork.infraestructura import utils
from exportacionsta.modulos.exportacion.infraestructura.despachadores import Despachador

def suscribirse_a_comandos():
    cliente= None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-notificaciones-estado', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='exportacion-sub-comandos', schema=AvroSchema(NotificacionEventoEstado))
        while True:
            mensaje = consumidor.receive()
            comando_integracion = mensaje.value().data
            print(f'Comando recibido: {mensaje.value().data}')

            print(f'Estado de la mensaje notificación: {comando_integracion.mensaje}')
            if comando_integracion.estado:
                comando_rollback = ComandoRollbackExportarImagen(
                    data= ComandoRollbackExportarImagenPayload(
                        id= comando_integracion.id_exportacion
                    )
                )

                despachador = Despachador()
                despachador.publicar_evento(comando_rollback, 'revertir-obtencion-imagenes')

            consumidor.acknowledge(mensaje)   

            
        cliente.close()
    except: 
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos():
    raise NotImplementedError