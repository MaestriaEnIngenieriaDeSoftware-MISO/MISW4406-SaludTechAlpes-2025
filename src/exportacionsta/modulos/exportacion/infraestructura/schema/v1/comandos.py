from pulsar.schema import *
from dataclasses import dataclass, field
from exportacionsta.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoObtenerImagenesPayload(ComandoIntegracion):
    tipo_imagen = String()
    tipo_patologia = String()

class ComandoObtenerImagenes(ComandoIntegracion):
    data = ComandoObtenerImagenesPayload()

class ComandoRollbackExportarImagenPayload(ComandoIntegracion):
    id = String()
    
class ComandoRollbackExportarImagen(ComandoIntegracion):
    data = ComandoObtenerImagenesPayload()
