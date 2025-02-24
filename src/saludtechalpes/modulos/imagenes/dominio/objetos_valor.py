from dataclasses import dataclass, field

@dataclass(frozen=True)
class Organo:
    nombre: str

@dataclass(frozen=True)
class EntornoClinico:
    tipo: str

@dataclass(frozen=True)
class SintomasNotasClinicas:
    sintomas: list

@dataclass(frozen=True)
class Historial:
    historial: list

@dataclass(frozen=True)
class ContextoProcesal:
    estado: str  
