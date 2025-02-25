from ..dominio.repositorios import RepositorioImagenes
from saludtechalpes.modulos.imagenes.infraestructura.dto import Imagen
from saludtechalpes.modulos.imagenes.aplicacion.dto import ObtenerImagenesDTO
from saludtechalpes.modulos.imagenes.infraestructura.mapeadores import MapeadorImagenes;
from saludtechalpes.seedwork.dominio.entidades import Entidad


class RepositorioImagenesPostgres(RepositorioImagenes):
        def consultar_entidades_por_parametros(self, query: ObtenerImagenesDTO) -> list[Entidad]:
                from saludtechalpes.config.db import db
                imagenes = db.session.query(Imagen).filter_by(tipo_patologia=query.tipo_patologia, tipo_imagen=query.tipo_imagen).all()
                return imagenes