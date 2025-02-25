from dataclasses import dataclass, field
import datetime
import uuid
from saludtechalpes.seedwork.aplicacion.dto import QueryDTO, DTO

@dataclass(frozen=True)
class ObtenerImagenesDTO(QueryDTO):
    tipo_patologia: str = field(default_factory=str)
    tipo_imagen: str = field(default_factory=str)

@dataclass(frozen=True)
class ImagenDTO(DTO):
    id: uuid.UUID = field(default_factory=uuid.uuid4),
    ruta_imagen_anonimizada: str = ""
    fecha_creacion: datetime = field(default_factory=lambda: datetime.now(datetime.timezone.utc)) 
    formato: str = field(default = "")

@dataclass(frozen=True)
class ImagenesDTO(DTO):
    imagenes: str = field(default_factory=list[ImagenDTO])