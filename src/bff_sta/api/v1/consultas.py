import strawberry
from .esquemas import *

@strawberry.type
class Query:
    imagenes: typing.List[Imagen] = strawberry.field(resolver=obtener_imagenes)