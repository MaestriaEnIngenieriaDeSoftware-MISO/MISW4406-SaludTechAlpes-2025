from saludtechalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado, ejecutar_query
from saludtechalpes.modulos.imagenes.dominio.entidades import Imagen
from saludtechalpes.modulos.imagenes.infraestructura.repositorios import RepositorioImagenes
from dataclasses import dataclass
from typing import List
from .base import ImagenesQueryBaseHandler

@dataclass
class ObtenerImagenes(Query):
    tipo_imagen: str
    tipo_patologia: str

class ObtenerImagenesHandler(ImagenesQueryBaseHandler):
    def handle(self, query: ObtenerImagenes) -> QueryResultado:
       repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenes.__class__)
       imagen = repositorio.obtener_todos(query.tipo_imagen, query.tipo_patologia)
       return QueryResultado(resultado=imagen)

@ejecutar_query.register(ObtenerImagenes)
def ejecutar_query_obtener_reserva(query: ObtenerImagenes):
    handler = ObtenerImagenesHandler()
    return handler.handle(query)