from dataclasses import dataclass
from exportacionsta.seedwork.dominio.fabricas import Fabrica
from exportacionsta.seedwork.dominio.repositorios import Repositorio
from exportacion.dominio.repositorios import RepositorioOperaciones
from .repositorios import RepositorioOperacionesPostgreSQL


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any =None) -> Repositorio:
        if obj == RepositorioOperaciones.__class__:
            return RepositorioOperacionesPostgreSQL()