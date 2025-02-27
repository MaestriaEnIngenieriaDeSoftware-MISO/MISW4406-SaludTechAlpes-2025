from dataclasses import dataclass, field
from exportacionsta.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class ExportarDTO(DTO):
    tipo_patologia: str = field(default_factory=str)
    tipo_imagen: str = field(default_factory=str)