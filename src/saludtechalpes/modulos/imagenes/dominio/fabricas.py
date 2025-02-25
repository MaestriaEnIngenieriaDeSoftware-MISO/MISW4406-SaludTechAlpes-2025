from .entidades import Imagen
from saludtechalpes.seedwork.dominio.repositorios import Mapeador
from saludtechalpes.seedwork.dominio.fabricas import Fabrica
from saludtechalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass
from saludtechalpes.modulos.imagenes.infraestructura.fabricas import FabricaRepositorio


@dataclass
class FabricaImagen(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, list):
            return mapeador.entidades_a_dto(obj)
        elif isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            imagen: Imagen = mapeador.dto_a_entidad(obj)
            return imagen