# recursos.py

import time
import threading
from logger import log_event
from datos_paciente import Paciente

# Recursos simulados
MAX_CAMAS = 3
MAX_DOCTORES = 2

# Semáforos para controlar el acceso a camas y doctores
semaforo_camas = threading.Semaphore(MAX_CAMAS)
semaforo_doctores = threading.Semaphore(MAX_DOCTORES)

def asignar_recursos(paciente: Paciente):
    """
    Asigna recursos limitados (cama y doctor) a un paciente usando semáforos.

    Parámetros:
    - paciente: Paciente al que se asignarán recursos.
    """
    log_event(f"{paciente.nombre} esperando recursos (cama/doctor)")

    # Espera hasta que haya cama disponible
    semaforo_camas.acquire()
    log_event(f"Cama asignada a {paciente.nombre}")

    # Espera hasta que haya doctor disponible
    semaforo_doctores.acquire()
    log_event(f"Doctor asignado a {paciente.nombre}")

    # Simula tiempo de tratamiento
    time.sleep(2 + paciente.prioridad)

    log_event(f"{paciente.nombre} terminó tratamiento. Liberando recursos.")

    # Libera los recursos
    semaforo_doctores.release()
    semaforo_camas.release()
