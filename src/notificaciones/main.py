import pulsar, _pulsar
from pulsar.schema import *
from .schema.v1.eventos import NotificacionEvento 
import uuid
import time
import os

def broker_host():
    return os.getenv('BROKER_HOST', default="localhost")

client = pulsar.Client(f'pulsar://{broker_host()}:6650')
consumer = client.subscribe('eventos-notificaciones', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='eventos-notificaciones', schema=AvroSchema(NotificacionEvento))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value())
    print('=========================================')

    print('==== Envía correo a usuario ====')

    consumer.acknowledge(msg)

client.close()