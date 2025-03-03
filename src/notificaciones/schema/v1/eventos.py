from pulsar.schema import *

class Evento(Record):
    id = String(default=str(uuid.uuid4()))

class NotificacionEvento(Evento):
    mensaje = String()
    cantidad_imagenes_exportadas = Integer()
    estado = String()
    timestamp = Long()