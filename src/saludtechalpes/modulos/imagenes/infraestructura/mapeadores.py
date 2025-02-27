from saludtechalpes.seedwork.dominio.repositorios import Mapeador
from saludtechalpes.modulos.imagenes.dominio.entidades import Imagen
from .dto import Imagen as ImagenDTO

class MapeadorImagen(Mapeador):
    def dto_a_entidad(seld, dto: ImagenDTO) -> Imagen:
        imagen = Imagen(dto.id, dto.ruta_imagen, dto.fecha_creacion, dto.formato)
        return imagen

    def obtener_tipo(self) -> type:
        return Imagen.__class__
    
    def entidad_a_dto(self, entidad: Imagen) -> ImagenDTO:
        raise NotImplementedError