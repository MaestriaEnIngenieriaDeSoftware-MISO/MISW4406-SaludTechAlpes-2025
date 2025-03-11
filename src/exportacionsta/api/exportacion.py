import exportacionsta.seedwork.presentacion.api as api
import json
from flask import request, Response
from exportacionsta.modulos.exportacion.aplicacion.mapeadores import MapeadorImagenesDTOJson
from exportacionsta.seedwork.dominio.excepciones import ExcepcionDominio
from exportacionsta.modulos.exportacion.aplicacion.comandos.exportar_imagenes import ExportarImagenes
from exportacionsta.seedwork.aplicacion.comandos import ejecutar_commando
from exportacionsta.modulos.sagas.coordinadores.saga_exportacion import CoordinadorSagaExportacion, oir_mensaje
from exportacionsta.modulos.exportacion.dominio.eventos import ExportacionImagenesIniciada
import uuid

bp = api.crear_blueprint('exportar', '/exportar')

@bp.route('/', methods=['POST'])
def exportar_Imagenes():
    try:
        saga = CoordinadorSagaAnonimizacion()
        saga.iniciar(uuid.UUID)

        imagenes_dict = request.json

        map_imagenes = MapeadorImagenesDTOJson()
        exportar_imagenes_dto = map_imagenes.externo_a_dto(imagenes_dict)

        comando = ExportacionImagenesIniciada(exportar_imagenes_dto.tipo_imagen,exportar_imagenes_dto.tipo_patologia)

        oir_mensaje(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')