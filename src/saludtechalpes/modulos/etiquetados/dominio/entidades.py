from dataclasses import dataclass, field
import src.saludtechalpes.modulos.etiquetados.dominio.objetos_valor as ov
import uuid
from src.seedwork.dominio.entidades import Entidad

@dataclass
class Etiquetado(Entidad):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    caracterizacion: ov.Caracterización = field(default_factory=ov.Caracterización)
    demografia: ov.Demografia = field(default_factory=ov.Demografia)