from saludtechalpes.config.db import db
from saludtechalpes.modulos.imagenes.dominio.repositorios import RepositorioImagenes
#from saludtechalpes.modulos.imagenes.dominio.objetos_valor import 
from saludtechalpes.modulos.imagenes.dominio.entidades import Imagen
#from saludtechalpes.modulos.imagenes.dominio.
from .dto import Imagen as ImagenDTO
from uuid import UUID
from saludtechalpes.modulos.imagenes.dominio.fabricas import FabricaImagenes
from .mapeadores import MapeadorImagen

class RepositorioImagenesSQLLite(RepositorioImagenes):

    def __init__(self):
        self._fabrica_imagenes: FabricaImagenes = FabricaImagenes()
    
    @property
    def fabrica_imagenes(self):
        return self._fabrica_imagenes

    def obtener_todos(self, tipo_imagen: str, tipo_patologia: str) -> list[Imagen]:
        imagenesDTO = db.session.query(ImagenDTO).filter_by(tipo_imagen=tipo_imagen, tipo_patologia=tipo_patologia).all()
        return [self.fabrica_imagenes.crear_objeto(imagenDTO, MapeadorImagen()) for imagenDTO in imagenesDTO]

    def agregar(self, entity: Imagen):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Imagen):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
    def obtener_por_id(self) -> list[Imagen]:
        # TODO
        raise NotImplementedError

        