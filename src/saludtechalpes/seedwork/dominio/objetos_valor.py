from dataclasses import dataclass

@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class Caracterización(ObjetoValor):
    resolucion: str
    contraste: str
    tipo: str
    fase_del_scaner: str

@dataclass(frozen=True)
class Organo(ObjetoValor):
    nombre: str

@dataclass(frozen=True)
class Demografia(ObjetoValor):
    grupo_edad: str
    sexo: str
    etnicidad: str

@dataclass(frozen)