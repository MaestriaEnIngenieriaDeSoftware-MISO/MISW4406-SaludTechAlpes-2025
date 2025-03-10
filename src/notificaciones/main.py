import pulsar, _pulsar
import random
from pulsar.schema import *
from schema.v1.eventos import NotificacionEvento 
import os

def broker_host():
    return os.getenv('BROKER_HOST', default="localhost")

def topico():
    return os.getenv('TOPICO', default="eventos-notificaciones")

def subscripcion():
    return os.getenv('SUBSCRIPCION', default="eventos-notificaciones")

client = pulsar.Client(f'pulsar://{broker_host()}:6650')
consumer = client.subscribe(topico(), consumer_type=_pulsar.ConsumerType.Shared, subscription_name=subscripcion(), schema=AvroSchema(NotificacionEvento))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value())
    print('=========================================')

    if random.choice([True, False]):
        print('==== Envía correo a usuario ====')
    else:
        print('==== No se envía correo a usuario ====')

    consumer.acknowledge(msg)

client.close()