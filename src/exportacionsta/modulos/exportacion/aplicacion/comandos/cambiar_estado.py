from exportacionsta.seedwork.aplicacion.comandos import ComandoHandler, Comando, ejecutar_commando as comando

from dataclasses import dataclass, field

@dataclass
class NotifiacionEnviada(Comando):
    id: str
    estado: str
    timestamp: datetime = field(default_factory=datetime.now)


class EnvioNotifiaccionesHandler(ComandoHandler):
    def handle(self,comando: NotifiacionEnviada):
        print("Se debe actualizar la bd con el cambio")

@comando.register(ExportarImagenes)
def ejecutar_comando_cambiar_estado_BD(comando: ExportarImagenes):
    handler = EnvioNotifiaccionesHandler()
    handler.handle(comando)