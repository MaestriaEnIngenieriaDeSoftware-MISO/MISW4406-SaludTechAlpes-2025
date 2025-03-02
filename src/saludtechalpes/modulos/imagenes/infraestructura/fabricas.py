from dataclasses import dataclass, field
from saludtechalpes.seedwork.dominio.fabricas import Fabrica
from saludtechalpes.seedwork.dominio.repositorios import Repositorio
from saludtechalpes.modulos.imagenes.dominio.repositorios import RepositorioImagenes
from .repositorios import RepositorioImagenesPostgreSQL

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioImagenes.__class__:
            return RepositorioImagenesPostgreSQL()
        