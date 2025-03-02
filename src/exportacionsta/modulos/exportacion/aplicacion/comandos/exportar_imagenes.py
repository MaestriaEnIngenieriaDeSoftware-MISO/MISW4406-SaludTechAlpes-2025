
from exportacionsta.seedwork.aplicacion.comandos import ComandoHandler, Comando, ejecutar_commando as comando

from dataclasses import dataclass, field
from exportacionsta.modulos.exportacion.infraestructura.despachadores import Despachador


@dataclass
class ExportarImagenes(Comando):
    tipo_imagen: str
    tipo_patologia: str


class ExportarImagenesHandler(ComandoHandler):

    def handle(self,comando: ExportarImagenes):
        despachador = Despachador()
        despachador.publicar_comando(comando,'comandos-obtener-imagenes')


@comando.register(ExportarImagenes)
def ejecutar_comando_exportar_imagenes(comando: ExportarImagenes):
    handler = ExportarImagenesHandler()
    handler.handle(comando)
    