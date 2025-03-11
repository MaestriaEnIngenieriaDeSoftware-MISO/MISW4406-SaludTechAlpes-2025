import pulsar
from pulsar.schema import *

from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.comandos import ComandoObtenerImagen, ComandoObtenerImagenPayload, ComandoRollbackExportarImagen, ComandoRollbackExportarImagenPayload
from saludtechalpes.seedwork.infraestructura import utils
from saludtechalpes.modulos.imagenes.infraestructura.schema.v1.eventos import EventoExportacionImagenesFinalizado, EventoExportacionImagenesFinalizadoPayload, EventoDatosAnonimizados, EventoDatosAnonimizadosPayload

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
        payload=ComandoRollbackExportarImagenPayload(
            id = '522416de-ca54-4ece-8de9-6b0de8a32554'
        )
        comando_integracion = ComandoRollbackExportarImagen(data = payload)
        self._publicar_mensaje(comando_integracion, 'revertir-obtencion-imagenes', AvroSchema(ComandoRollbackExportarImagen))

    def publicar_evento(self, evento, topico):
        if isinstance(evento, EventoExportacionImagenesFinalizado):

            payload = EventoExportacionImagenesFinalizadoPayload(
                mensaje = evento.data.mensaje,
                cantidad_imagenes_exportadas= evento.data.cantidad_imagenes_exportadas,
                estado = evento.data.estado,
                timestamp = int(datetime.datetime.now().timestamp())
            )

            evento_integracion = EventoExportacionImagenesFinalizado(data = payload)
            self._publicar_mensaje(evento_integracion, topico, schema= AvroSchema(EventoExportacionImagenesFinalizado))

        elif isinstance(evento, EventoDatosAnonimizados):
            payload = EventoDatosAnonimizadosPayload(
                id = evento.data.id,
                estado = evento.data.estado
            )
            evento_integracion = EventoDatosAnonimizados( data=payload)
            self._publicar_mensaje(evento_integracion, topico, schema = AvroSchema(EventoDatosAnonimizados))
