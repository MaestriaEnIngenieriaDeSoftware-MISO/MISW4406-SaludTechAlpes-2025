from abc import ABC, abstractmethod
from .repositorios import Mapeador

class Fabrica(ABC):
    @abstractmethod
    def crear_objeto(self, obj: any, mapeador: Mapeador=None) -> any:
        ...