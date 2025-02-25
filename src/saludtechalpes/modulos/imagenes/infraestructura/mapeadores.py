from ....seedwork.dominio.repositorios import Mapeador;
from saludtechalpes.modulos.imagenes.dominio.entidades import Imagen
from saludtechalpes.modulos.imagenes.aplicacion.dto import ImagenDTO, ImagenesDTO

class MapeadorImagenes(Mapeador):
    
    def entidad_a_dto(self, entidad: Imagen) -> ImagenDTO:     
        imagenDTO = ImagenDTO(id = entidad.id, ruta_imagen_anonimizada=entidad.ruta_imagen_anonimizada, fecha_creacion=entidad.fecha_creacion)
        return imagenDTO

    def entidades_a_dto(self, entidades: list[Imagen]) -> ImagenesDTO:     
        imagenesDTO:list[ImagenDTO] = list()
        for imagen in entidades:
            imagenDTO = self.entidad_a_dto(imagen)
            imagenesDTO.append(imagenDTO)
        return ImagenesDTO(imagenesDTO)

