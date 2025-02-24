from dataclasses import dataclass, field

@dataclass(frozen=True)
class Caracterización:
    resolucion: str
    contraste: str
    tipo: str
    fase_del_scaner: str

@dataclass(frozen=True)
class Demografia:
    grupo_edad: str
    sexo: str
    etnicidad: str