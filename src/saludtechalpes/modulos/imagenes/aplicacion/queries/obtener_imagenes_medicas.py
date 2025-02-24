from src.saludtechalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado, ejecutar_query
from src.saludtechalpes.config.db import db
from src.saludtechalpes.modulos.imagenes.dominio.entidades import Imagen
from dataclasses import dataclass
from typing import List

@dataclass
class ObtenerImagenes(Query):
    tipo_patologia: str
    tipo_imagen: str

@dataclass
class ImagenResultado(QueryResultado):
    resultado: List[Imagen]

class ObtenerImagenesHandler(QueryHandler):
    def handle(self, query: ObtenerImagenes) -> ImagenResultado:
        # Lógica para obtener las imágenes filtradas
        imagenes = db.session.query(Imagen).filter_by(
            tipo_patologia=query.tipo_patologia,
            tipo_imagen=query.tipo_imagen
        ).all()
        return ImagenResultado(resultado=imagenes)

@ejecutar_query.register
def _(query: ObtenerImagenes) -> QueryResultado:
    handler = ObtenerImagenesHandler()
    return handler.handle(query)