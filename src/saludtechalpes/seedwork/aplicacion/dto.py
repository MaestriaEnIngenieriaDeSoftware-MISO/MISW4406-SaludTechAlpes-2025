from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=False)
class DTO(ABC):
    ...

class QueryDTO(DTO):
    ...

class Mapeador(ABC):
    @abstractmethod
    def externo_a_dto(self, externo: any) -> DTO:
        ...

    @abstractmethod
    def dto_a_externo(self, dto: DTO) -> any:
        ...
    