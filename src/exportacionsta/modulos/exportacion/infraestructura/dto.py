from exportacionsta.config.db import db
from sqlalchemy.orm import declarative_base
from sqlalchemy import Enum, func
import enum

Base = db.declarative_base()

class EstadoDeOperacion(enum.Enum):
    INICIADO = "iniciado"
    INCOMPLETO = "incompleto"
    FINALIZADO = "finalizado"

class Operaciones(db.Model):
    __tablename__  = "operaciones"
    id = db.Column(db.String, primary_key=True)
    estado = db.Column(Enum(EstadoDeOperacion))
    fecha_creacion = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    fecha_actualizacion = db.Column(db.DateTime(timezone=True), nullable=True)