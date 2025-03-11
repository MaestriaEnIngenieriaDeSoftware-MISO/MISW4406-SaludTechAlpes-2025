from .entidades import Operacion
from saludtechalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from saludtechalpes.seedwork.dominio.fabricas import Fabrica
from saludtechalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaOperaciones(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Operacion.__class__:
            operacion: Operacion = mapeador.dto_a_entidad(obj)
            return operacion
        elif isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)