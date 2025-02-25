from dataclasses import dataclass
from saludtechalpes.seedwork.dominio.fabricas import Fabrica
from saludtechalpes.seedwork.dominio.repositorios import Repositorio
from saludtechalpes.modulos.imagenes.dominio.repositorios import RepositorioImagenes
from saludtechalpes.modulos.imagenes.infraestructura.repositorios import RepositorioImagenesPostgres
from saludtechalpes.seedwork.dominio.excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioImagenes.__class__:
            return RepositorioImagenesPostgres()
        else:
            raise ExcepcionFabrica()