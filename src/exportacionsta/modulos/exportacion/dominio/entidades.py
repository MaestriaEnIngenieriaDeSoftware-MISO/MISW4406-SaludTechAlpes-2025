from dataclasses import dataclass, field
import saludtechalpes.modulos.imagenes.dominio.objetos_valor as ov
import uuid
from datetime import datetime, timezone
from exportacionsta.seedwork.dominio.entidades import Entidad
from exportacionsta.modulos.exportacion.dominio.objetos_valor import Estado

@dataclass
class Operacion(Entidad):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    estado: Estado = field(default_factory=Estado.INICIADO)
    fecha_creacion: datetime = field(default_factory=lambda: datetime.now(timezone.utc))