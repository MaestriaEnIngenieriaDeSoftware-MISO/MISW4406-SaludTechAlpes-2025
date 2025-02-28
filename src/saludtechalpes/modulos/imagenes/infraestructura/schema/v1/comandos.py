from pulsar.schema import *
from dataclasses import dataclass, field
from saludtechalpes.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

class ComandoObtenerImagenPayload(ComandoIntegracion):
    id: String()

class ComandoObtenerImagen(ComandoIntegracion):
    data = ComandoObtenerImagenPayload()