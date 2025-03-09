from saludtechalpes.seedwork.aplicacion.comandos import Comando, ComandoHandler
from dataclasses import dataclass, field
from saludtechalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from saludtechalpes.config.db import db
from saludtechalpes.modulos.imagenes.infraestructura.dto import ImagenesExportadas
@dataclass
class EliminarRegistrosExportados(Comando):
    id: str

class EliminarRegistrosExportadosHandler(ComandoHandler):
    def handle(self, comando: EliminarRegistrosExportados):
        db.session.query(ImagenesExportadas).filter_by(id = comando.id).delete()
        db.session.commit()

@comando.register(EliminarRegistrosExportados)
def ejecutar_commando_eliminar_registros_exportados(comando: EliminarRegistrosExportados):
    handler = EliminarRegistrosExportadosHandler()
    handler.handle(comando)