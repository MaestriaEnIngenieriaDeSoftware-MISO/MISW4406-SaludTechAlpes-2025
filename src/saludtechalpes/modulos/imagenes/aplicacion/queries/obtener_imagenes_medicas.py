from saludtechalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado, ejecutar_query
from saludtechalpes.modulos.imagenes.dominio.entidades import Imagen
from saludtechalpes.modulos.imagenes.infraestructura.repositorios import RepositorioImagenes
from dataclasses import dataclass
from typing import List
from .base import ImagenesQueryBaseHandler

@dataclass
class ObtenerImagenes(Query):
    id: str


class ObtenerImagenesHandler(ImagenesQueryBaseHandler):
    def handle(self, query: ObtenerImagenes) -> QueryResultado:
       repositorio = self.fabrica_repositorio.crear_objeto(RepositorioImagenes.__class__)
       imagen = repositorio.obtener_por_id(query.id)
       return QueryResultado(resultado=imagen)

@ejecutar_query.register(ObtenerImagenes)
def ejecutar_query_obtener_reserva(query: ObtenerImagenes):
    handler = ObtenerImagenesHandler()
    return handler.handle(query)