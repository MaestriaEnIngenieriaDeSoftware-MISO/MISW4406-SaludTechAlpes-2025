from saludtechalpes.config import db
from sqlalchemy.orm import declarative_base

Base = db.declarative_base()

class Imagen(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.String, primary_key=True)
    ruta_imagen_anonimizada = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    formato = db.Column(db.String, nullable=False)
    ## metadata: Metadata = field(default_factory=Metadata)
    ## region_anatomica: RegionAnatomica = field(default_factory=RegionAnatomica)