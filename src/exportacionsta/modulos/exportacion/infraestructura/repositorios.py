from saludtechalpes.config.db import db
from .dto import Operaciones as OperacionesDTO
from uuid import UUID

from exportacionsta.modulos.exportacion.dominio.repositorios import RepositorioOperaciones
from exportacionsta.modulos.exportacion.dominio.fabricas import FabricaOperaciones

class RepositorioOperacionesPostgreSQL(RepositorioOperaciones):

    def __init__(self):
        self._fabrica_operaciones: FabricaOperaciones = FabricaOperaciones()

    @property
    def fabrica_operaciones(self):
        return self._fabrica_operaciones

    def obtener_todos(self) -> list[OperacionesDTO]:
        ...

    def agregar(self, entity: OperacionesDTO):
        db.session.add(entity)   
        db.session.commit()  
        # raise NotImplementedError

    def actualizar(self, entity: OperacionesDTO):
        operacion = db.session.query(OperacionesDTO).filter(OperacionesDTO.id==entity.id).first()
        if (operacion is not None):
            operacion.estado = entity.estado
            db.session.commit()

    def eliminar(self, entity_id: UUID):
        operacion = db.session.query(OperacionesDTO).filter(OperacionesDTO.id==entity_id).first()
        db.session.delete(operacion)
        db.session.commit()
    
    def obtener_por_id(self) -> list[OperacionesDTO]:
        # TODO
        raise NotImplementedError