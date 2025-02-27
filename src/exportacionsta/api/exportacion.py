import exportacionsta.seedwork.presentacion.api as api
import json
from flask import request, Response
from exportacionsta.modulos.exportacion.aplicacion.mapeadores import MapeadorImagenesDTOJson
from exportacionsta.seedwork.dominio.excepciones import ExcepcionDominio
from exportacionsta.modulos.exportacion.aplicacion.servicios import ServicioExportacion

bp = api.crear_blueprint('exportar', '/exportar')

@bp.route('/', methods=['POST'])
def exportar_Imagenes():
    try:
        imagenes_dict = request.json

        map_imagenes = MapeadorImagenesDTOJson()
        exportar_imagenes_dto = map_imagenes.externo_a_dto(imagenes_dict)

        se = ServicioExportacion()
        dto_final = se.exportar_imagenes(exportar_imagenes_dto)

        return map_imagenes.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')