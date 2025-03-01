from dataclasses import dataclass, field
from saludtechalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ImagenDTO(DTO):
    id: str
    ruta_imagen: str
    fecha_creacion: str
    metadatos: str
    formato: str