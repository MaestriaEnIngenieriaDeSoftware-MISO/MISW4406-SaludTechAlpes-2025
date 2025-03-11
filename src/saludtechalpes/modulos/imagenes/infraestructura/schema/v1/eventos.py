from pulsar.schema import *
from saludtechalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class EventoExportacionImagenesFinalizadoPayload(Record):
    id = String()
    mensaje = String()
    cantidad_imagenes_exportadas = Integer()
    estado = String()
    timestamp = Long()

class EventoExportacionImagenesFinalizado(EventoIntegracion):
    data = EventoExportacionImagenesFinalizadoPayload()

class EventoDatosAnonimizadosPayload(Record):
    id = String()
    estado = String()

class EventoDatosAnonimizados(EventoIntegracion):
    data = EventoDatosAnonimizadosPayload()

