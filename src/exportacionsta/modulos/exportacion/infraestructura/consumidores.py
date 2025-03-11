import pulsar, _pulsar
from pulsar.schema import *
import uuid
import datetime
from exportacionsta.modulos.exportacion.dominio.eventos import NotificacionEnviadaSatisfactoriamente, NotificacionFallida, ExportacionImagenesFinalizada, ExportacionImagenesFallida
from exportacionsta.modulos.sagas.coordinadores.saga_exportacion import CoordinadorSagaExportacion, oir_mensaje

def suscribirse_a_eventos_notificaciones():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('revertir-exportacion', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='eventos-notifiacion', schema=AvroSchema(NotificacionEnviadaSatisfactoriamente))
        while True:
            saga = CoordinadorSagaExportacion()
            mensaje = consumidor.receive()
            evento_integracion = mensaje.value().data
            print(f'------> Evento recibido: {evento_integracion}')

            if evento_integracion.estado == 'EXITOSO':
                notificacion_eviada = NotificacionEnviadaSatisfactoriamente(
                    id=evento_integracion.id,
                    estado = evento_integracion.estado,
                    timestamp = int(datetime.datetime.now().timestamp())
                )
                oir_mensaje(notificacion_eviada)
            else:
                notificacion_eviada = NotificacionFallida(
                    id=evento_integracion.id,
                    estado = evento_integracion.estado,
                    timestamp = int(datetime.datetime.now().timestamp())
                )
                oir_mensaje(notificacion_eviada)
            consumidor.acknowledge(mensaje)
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos notificaciones!')
        traceback.print_exc()
        if cliente:
            cliente.close()   

def suscribirse_a_eventos_exportaciones():
    saga = CoordinadorSagaExportacion()
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-datos-anonimizados', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='eventos-exportacion', schema=AvroSchema(ExportacionImagenesFinalizada))
        while True:
            saga = CoordinadorSagaExportacion()
            mensaje = consumidor.receive()
            evento_integracion = mensaje.value().data
            print(f'------> Evento recibido: {evento_integracion}')

            if evento_integracion.estado == 'EXITOSO':
                evento_exportacion = ExportacionImagenesFinalizada(
                    id=evento_integracion.id,
                    estado = evento_integracion.estado,
                )
                oir_mensaje(evento_exportacion)
            else:
                evento_exportacion = ExportacionImagenesFallida(
                    id=evento_integracion.id,
                    estado = evento_integracion.estado,
                )
                oir_mensaje(evento_exportacion)
            consumidor.acknowledge(mensaje)
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos exportaciones!')
        traceback.print_exc()
        if cliente:
            cliente.close() 