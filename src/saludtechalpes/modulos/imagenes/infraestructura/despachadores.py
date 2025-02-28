import pulsar
from pulsar.schema import *

from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.comandos import ComandoObtenerImagen, ComandoObtenerImagenPayload
from saludtechalpes.seedwork.infraestructura import utils
from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.eventos import EventoExportacionImagenesFinalizado, EventoExportacionImagenesFinalizadoPayload

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

    def publicar_comando(self):
        payload=ComandoObtenerImagenPayload(
            tipo_imagen = 'aaaa',
            tipo_patologia = 'aaaa'
        )
        comando_integracion = ComandoObtenerImagen(data = payload)
        self._publicar_mensaje(comando_integracion, 'comandos-obtener-imagenes', AvroSchema(ComandoObtenerImagen))

    def publicar_evento(self, evento, topico):
        payload = EventoExportacionImagenesFinalizadoPayload(
            mensaje = evento.data.mensaje,
            cantidad_imagenes_exportadas= evento.data.cantidad_imagenes_exportadas,
            estado = evento.data.estado,
            timestamp = int(datetime.datetime.now().timestamp())
        )

        evento_integracion = EventoExportacionImagenesFinalizado(data = payload)
        self._publicar_mensaje(evento_integracion, topico, schema= AvroSchema(EventoExportacionImagenesFinalizado))
