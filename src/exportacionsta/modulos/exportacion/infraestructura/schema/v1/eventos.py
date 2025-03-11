from pulsar.schema import *
from exportacionsta.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ExportacionImagenesFinalizadaPayload(Record):
    id= String()
    estado = String()

class ExportacionImagenesFinalizada(Record):
    data = ExportacionImagenesFinalizadaPayload()

class NotificacionEnviadaPayload(Record):
    id = String()
    estado = String()

class NotificacionEnviada(Record):
    data = NotificacionEnviadaPayload()