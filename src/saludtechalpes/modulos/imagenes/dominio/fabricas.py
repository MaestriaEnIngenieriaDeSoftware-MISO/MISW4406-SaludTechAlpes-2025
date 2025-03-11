from .entidades import Imagen
from exportacionsta.seedwork.dominio.repositorios import Mapeador, Repositorio
from exportacionsta.seedwork.dominio.fabricas import Fabrica
from exportacionsta.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaImagenes(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Imagen.__class__:
            imagen: Imagen = mapeador.dto_a_entidad(obj)
            return imagen