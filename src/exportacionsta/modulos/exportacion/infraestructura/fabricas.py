from dataclasses import dataclass, field
from exportacionsta.seedwork.dominio.fabricas import Fabrica
from exportacionsta.seedwork.dominio.repositorios import Repositorio


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any =None) -> Repositorio:
        if obj == RepositorioExportarcion.__class__:
            return RepositoroReservasPostgreSQL()