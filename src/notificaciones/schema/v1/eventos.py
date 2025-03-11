from pulsar.schema import *
import uuid
import time


def time_millis():
    return int(time.time() * 1000)

class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class EventoExportacionImagenesFinalizadoPayload(Record):
    id = String()
    mensaje = String()
    cantidad_imagenes_exportadas = Integer()
    estado = String()
    timestamp = Long()

class NotificacionEventoEstadoPayload(Record):
    id_exportacion = String()
    mensaje = String()
    estado = Boolean()
    timestamp = Long()

class NotificacionEvento(EventoIntegracion):
    data = EventoExportacionImagenesFinalizadoPayload()

class NotificacionEventoEstado(EventoIntegracion):
    data = NotificacionEventoEstadoPayload()