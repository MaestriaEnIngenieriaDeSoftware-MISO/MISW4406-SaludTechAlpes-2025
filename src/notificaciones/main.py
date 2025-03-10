import pulsar, _pulsar
import random
from pulsar.schema import *
from schema.v1.eventos import NotificacionEvento, NotificacionEventoEstadoPayload, NotificacionEventoEstado,  time_millis
import os



def broker_host():
    return os.getenv('BROKER_HOST', default="localhost")

def topico():
    return os.getenv('TOPICO', default="eventos-notificaciones")

def topico_estado():
    return os.getenv('TOPICO_ESTADO', default="eventos-notificaciones-estado")

def subscripcion():
    return os.getenv('SUBSCRIPCION', default="eventos-notificaciones")

client = pulsar.Client(f'pulsar://{broker_host()}:6650')
consumer = client.subscribe(topico(), consumer_type=_pulsar.ConsumerType.Shared, subscription_name=subscripcion(), schema=AvroSchema(NotificacionEvento))
publisher = client.create_producer(topico_estado(), schema=AvroSchema(NotificacionEventoEstado))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value())
    print('=========================================')

    if random.choice([True, False]):
        print('==== Envía correo a usuario ====')
        evento_estado = NotificacionEventoEstado(
            data=NotificacionEventoEstadoPayload(
                id_exportacion= msg.value().data.id,
                mensaje="Correo enviado exitosamente",
                estado=True,
                timestamp=time_millis()
            )
        )
    else:
        print('==== No se envía correo a usuario ====')
        evento_estado = NotificacionEventoEstado(
            data=NotificacionEventoEstadoPayload(
                id_exportacion= msg.value().data.id,
                mensaje="No se pudo enviar el correo",
                estado=False,
                timestamp=time_millis()
            )
        )

    publisher.send(evento_estado)
    consumer.acknowledge(msg)

client.close()