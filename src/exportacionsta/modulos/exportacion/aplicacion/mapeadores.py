
from exportacionsta.seedwork.aplicacion.dto import Mapeador as AppMap
from .dto import ExportarDTO


class MapeadorImagenesDTOJson(AppMap):
    def externo_a_dto(self, externo:dict) -> ExportarDTO:
        exportar_dto = ExportarDTO()
        return exportar_dto

    def dto_a_externo(self, dto: ExportarDTO) -> dict:
        return dto.__dict__