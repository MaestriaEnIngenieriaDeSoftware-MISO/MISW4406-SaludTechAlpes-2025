from abc import ABC, abstractmethod
from uuid import UUID
from .entidades import Entidad
from ..aplicacion.dto import QueryDTO;
from saludtechalpes.modulos.imagenes.aplicacion.dto import DTO

class Repositorio(Entidad):
    @abstractmethod
    def consultar_entidades_por_parametros(self, query: QueryDTO) -> DTO:
        ...

    @abstractmethod
    def registrar_entidad(self, imagen: Entidad) -> Entidad:
        ...

    @abstractmethod
    def registrar_entidades(self, imagenes: list[Entidad]) -> list[Entidad]:
        ...


class Mapeador(ABC):
    @abstractmethod
    def entidad_a_dto(self, entidad: Entidad) -> any:
        ...

    @abstractmethod
    def dto_a_entidad(self, dto: any) -> Entidad:
        ...

    @abstractmethod
    def entidades_a_dto(self, entidad: list[Entidad]) -> any:
        ... 