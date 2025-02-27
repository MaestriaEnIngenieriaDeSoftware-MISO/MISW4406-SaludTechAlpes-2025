from saludtechalpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

Base = db.declarative_base()

class Imagen(db.Model):
    __tablename__  = "imagenes"
    id = db.Column(db.String, primary_key=True)
    ruta_imagen = db.Column(db.String)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    metadatos = db.Column(db.String) 
    formato = db.Column(db.String)