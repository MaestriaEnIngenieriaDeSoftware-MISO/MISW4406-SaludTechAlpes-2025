from dataclasses import dataclass, field
import src.saludtechalpes.modulos.imagenes.dominio.objetos_valor as ov
import uuid
from datetime import datetime, timezone
from src.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Imagen(AgregacionRaiz):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    ruta_imagen_anonimizada: str = ""
    fecha_creacion: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: Metadata = field(default_factory=Metadata)
    region_anatomica = field(default_factory=RegionAnatomica)
    formato: str

@dataclass
class Metadata(Entidad):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    entorno_clinico: ov.EntornoClinico = field(default_factory = ov.EntornoClinico)
    sintomas: ov.SintomasNotasClinicas = field(default_factory = ov.SintomasNotasClinicas)
    historial : ov.Historial = field(default_factory = ov.Historial)
    contexto_procesal: ov.ContextoProcesal = field(default_factory = ov.ContextoProcesal)
    token_paciente: uuid.UUID = field(default_factory=uuid.uuid4)

@dataclass
class RegionAnatomica(Entidad):
    nombre_region: str
    organo: ov.Organo = field(default_factory = ov.Organo)