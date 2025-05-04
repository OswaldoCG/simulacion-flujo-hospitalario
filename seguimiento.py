# seguimiento.py

import time
import threading
from logger import log_event
from datos_paciente import Paciente

def seguimiento_paciente(paciente: Paciente):
    """
    Simula el seguimiento clínico post-diagnóstico antes del alta del paciente.

    Parámetros:
    - paciente: Paciente que será monitoreado.
    """
    log_event(f"Iniciando seguimiento para {paciente.nombre} (ID: {paciente.id})")

    # Simula revisiones periódicas
    for ronda in range(3):
        time.sleep(1 + paciente.prioridad * 0.5)
        log_event(f"Revisión {ronda+1} completada para {paciente.nombre}")

    log_event(f"{paciente.nombre} ha sido dado de alta del sistema hospitalario")

def iniciar_seguimiento_concurrente(pacientes):
    """
    Ejecuta seguimiento en hilos concurrentes para varios pacientes.

    Parámetros:
    - pacientes: lista de objetos Paciente.
    """
    threads = []
    for paciente in pacientes:
        t = threading.Thread(target=seguimiento_paciente, args=(paciente,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
