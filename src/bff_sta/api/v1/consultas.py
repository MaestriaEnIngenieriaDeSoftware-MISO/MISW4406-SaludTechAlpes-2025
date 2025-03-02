import strawberry
from .esquemas import *

@strawberry.type
class Query:
    @strawberry.field
    def imagenes(self, tipo_patologia: str, tipo_imagen: str) -> StatusResponse:
        return obtener_imagenes(self, tipo_patologia, tipo_imagen)