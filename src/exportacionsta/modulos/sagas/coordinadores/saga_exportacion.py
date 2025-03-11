import uuid

from exportacionsta.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Paso, Transaccion, Inicio, Fin
from exportacionsta.modulos.sagas.comandos.eliminar_imagenes_exportadas import EliminarImagenesExportadas
from exportacionsta.seedwork.dominio.eventos import EventoDominio
from exportacionsta.modulos.exportacion.aplicacion.comandos import exportar_imagenes, cambiar_estado
from exportacionsta.modulos.sagas.comandos import eliminar_imagenes_exportadas
from exportacionsta.modulos.exportacion.dominio.eventos import ExportacionImagenesIniciada, ExportacionImagenesFallida,NotificacionEnviadaSatisfactoriamente, NotificacionFallida


class CoordinadorSagaExportacion(CoordinadorOrquestacion):
    def __init__(self):
        super().__init__()
        self.id_correlacion = str(uuid.uuid4())
        #self.repositorio_saga_log = RepositorioSagaLogPostgresSQL()
        self.inicializar_pasos()

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=exportar_imagenes.ejecutar_comando_exportar_imagenes, evento=ExportacionImagenesIniciada, error=ExportacionImagenesFallida, compensacion=eliminar_imagenes_exportadas.ejecutar_comando_rollback_imagenes_exportadas ,exitosa=True),
            Transaccion(index=2, comando=cambiar_estado.ejecutar_comando_cambiar_estado_BD, evento=NotificacionEnviadaSatisfactoriamente, error=NotificacionFallida, compensacion=cambiar_estado.ejecutar_comando_cambiar_estado_BD ,exitosa=True),
            Fin()
        ]

    def construir_comando(self, evento:EventoDominio, tip_comando:type) -> Comando:
        if isinstance(evento, ExportacionImagenesIniciada):
            return exportar_imagenes.ejecutar_comando_exportar_imagenes(
                tipo_imagen=evento.tipo_imagen,
                tipo_patologia=evento.tipo_patologia
            )
        elif isinstance(evento, ExportacionImagenesFallida):
            return eliminar_imagenes_exportadas.ejecutar_comando_rollback_imagenes_exportadas(
                id = evento.id
            )
        elif isinstance(evento, NotificacionEnviadaSatisfactoriamente):
            return cambiar_estado.ejecutar_comando_cambiar_estado_BD(
                id = evento.id,
                estado = evento.estado,
                timestamp = evento.timestamp
            )
        elif isinstance(evento, NotificacionFallida):
            return cambiar_estado.ejecutar_comando_cambiar_estado_BD(
                id = evento.id,
                estado = evento.estado,
                timestamp = evento.timestamp
            )
        else:
            raise NotImplementedError
    
    def procesar_evento(self, evento: EventoDominio):
        paso, index = self.obtener_paso_dado_un_evento(evento)
        if self.es_ultima_transaccion(index) and not isinstance(evento, paso.error):
            self.terminar()
        
        if isinstance(evento, paso.error):
            if index > 0 and self.pasos[index].compensacion:
                self.publicar_comando(evento, self.pasos[index].compensacion)
                self.id_correlacion = evento.proceso_id
                self.persistir_en_saga_log(evento)
        
        elif isinstance(evento, paso.evento):
            if index < len(self.pasos) - 1:
                #siguiente_paso = self.pasos[index + 1]
                self.publicar_comando(evento, paso.comando)
                self.id_correlacion = evento.proceso_id
                self.persistir_en_saga_log(evento)

    def iniciar(self, id_proceso_exportacion):
        self.id_correlacion = id_proceso_exportacion
        self.persistir_en_saga_log({"tipo_evento":"Inicio","mensaje": f"Se inicia SAGA: {id_proceso_anonimizacion}"})
        
    def terminar(self, id_proceso_exportacion):
        self.id_correlacion = id_proceso_exportacion
        self.persistir_en_saga_log({"tipo_evento":"Fin", "mensaje": f"Se finaliza SAGA: {id_proceso_anonimizacion}"})
        
        
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")


def publicar_evento_integracion(mensaje, topico):
    despachador = Despachador()
    despachador.publicar_evento(mensaje, topico)