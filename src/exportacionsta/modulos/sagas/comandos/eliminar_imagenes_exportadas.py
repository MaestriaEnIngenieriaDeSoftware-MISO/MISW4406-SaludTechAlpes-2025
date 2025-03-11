from exportacionsta.seedwork.aplicacion.comandos import Comando, ComandoHandler
from exportacionsta.modulos.exportacion.infraestructura.despachadores import Despachador
from exportacionsta.modulos.exportacion.infraestructura.schema.v1.comandos import ComandoRollbackExportarImagenPayload, ComandoRollbackExportarImagen


class EliminarImagenesExportadas(Comando):
    id: str

class EliminarImagenesExportadasHandler(ComandoHandler):
    def handle(self, comando: EliminarImagenesExportadas):
        payload = ComandoRollbackExportarImagenPayload(
            id= comando.id
        )
        comando = ComandoRollbackExportarImagen(data = payload)
        despachador = Despachador()
        despachador.publicar_comando(comando, 'revertir-obtencion-imagenes', AvroSchema(ComandoRollbackExportarImagen))


@comando.register(EliminarImagenesExportadas)
def ejecutar_comando_rollback_imagenes_exportadas(comando: EliminarImagenesExportadas):
    handler = EliminarImagenesExportadasHandler()
    handler.handle(comando)