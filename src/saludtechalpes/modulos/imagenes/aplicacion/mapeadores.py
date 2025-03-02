from saludtechalpes.seedwork.aplicacion.dto import Mapeador
from .dto import ImagenDTO
class MapeadorImagenDTOJson(Mapeador):
    def dto_a_externo(self, dto: ImagenDTO) -> dict:
        return dto.__dict__    
    
    def externo_a_dto(self, externo: dict) -> ImagenDTO:
        raise NotImplementedError