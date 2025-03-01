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

    def obtener_por_id(self, id:UUID) -> ImagenDTO:
        imagenDTO = db.session.query(ImagenDTO).filter_by(id=str(id)).one()
        return self.fabrica_imagenes.crear_objeto(imagenDTO, MapeadorImagen())
    def agregar(self, entity: Imagen):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Imagen):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
    def obtener_todos(self) -> list[Imagen]:
        # TODO
        raise NotImplementedError

        