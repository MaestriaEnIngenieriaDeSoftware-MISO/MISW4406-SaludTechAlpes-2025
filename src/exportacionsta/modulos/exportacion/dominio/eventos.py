from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
import uuid
from exportacionsta.seedwork.dominio.eventos import EventoDominio


@dataclass
class ExportacionImagenesIniciada(EventoDominio):
    id: uuid.UUID = None
    tipo_imagen: str
    tipo_patologia: str
    fecha: datetime = field(default_factory=datetime.now)


@dataclass
class ExportacionImagenesFinalizada(EventoDominio):
    id: uuid.UUID = None
    estado: str
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class ExportacionImagenesFallida(EventoDominio):
    id: uuid.UUID = None
    estado: str
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class NotificacionEnviadaSatisfactoriamente(EventoDominio):
    id: uuid.UUID = None
    estado: str
    timestamp: datetime = field(default_factory=datetime.now)

class NotificacionFallida(EventoDominio):
    id: uuid.UUID = None
    estado: str
    timestamp: datetime = field(default_factory=datetime.now)