from dataclasses import dataclass, field
from exportacionsta.seedwork.aplicacion.dto import DTO
from exportacionsta.modulos.exportacion.dominio.objetos_valor import Estado

@dataclass(frozen=True)
class ExportarDTO(DTO):
    tipo_patologia: str = field(default_factory=str)
    tipo_imagen: str = field(default_factory=str)

@dataclass(frozen=True)
class RegistrarOperacionDTO(DTO):
    estado: str = field(default_factory=Estado)