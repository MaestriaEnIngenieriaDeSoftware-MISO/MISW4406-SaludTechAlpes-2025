import pulsar
from pulsar.schema import *

from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.comandos import ComandoObtenerImagen, ComandoObtenerImagenPayload
from saludtechalpes.seedwork.infraestructura import utils

import datetime
epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoObtenerImagen))
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando(self):
        payload=ComandoObtenerImagenPayload(
            id= '1'
        )
        comando_integracion = ComandoObtenerImagen(data = payload)
        self._publicar_mensaje(comando_integracion, 'comandos-obtener-imagenes', AvroSchema(ComandoObtenerImagen))