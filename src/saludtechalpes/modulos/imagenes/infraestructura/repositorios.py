from ..dominio.repositorios import RepositorioImagenes
from saludtechalpes.config.db import db
from saludtechalpes.modulos.imagenes.dominio.entidades import Imagen
from saludtechalpes.modulos.imagenes.aplicacion.dto import ImagenDTO, ImagenesDTO, DTO, ObtenerImagenesDTO
from saludtechalpes.modulos.imagenes.infraestructura.mapeadores import MapeadorImagenes;

class RepositorioImagenesPostgres(RepositorioImagenes):
        def consultar_entidades_por_parametros(self, query: ObtenerImagenesDTO) -> DTO:
                mapeador = MapeadorImagenes()
                imagenes = db.session.query(Imagen).filter_by(tipo_patologia=query.tipo_patologia, tipo_imagen=query.tipo_imagen).all()
                imagenesDTO:list[ImagenDTO] = list()
                for imagen in imagenes:
                    imagenDTO = mapeador.entidad_a_dto(imagen)
                    imagenesDTO.append(imagenDTO)
                return ImagenesDTO(imagenesDTO)