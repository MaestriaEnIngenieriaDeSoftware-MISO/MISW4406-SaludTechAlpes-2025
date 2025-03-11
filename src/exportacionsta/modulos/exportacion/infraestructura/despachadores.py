import pulsar
from pulsar.schema import *

from exportacionsta.seedwork.infraestructura import utils
from exportacionsta.modulos.exportacion.infraestructura.schema.v1.comandos import ComandoObtenerImagenes, ComandoObtenerImagenesPayload, ComandoRollbackExportarImagenPayload
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_comando(self,comando, topico):
        payload=ComandoRollbackExportarImagenPayload(
            id= comando.data.id,
        )
        comando_integracion = ComandoRollbackExportarImagen(data = payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoRollbackExportarImagen))
