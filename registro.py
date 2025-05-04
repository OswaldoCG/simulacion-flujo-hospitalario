# registro.py

import threading
from logger import log_event
from datos_paciente import Paciente

def registrar_paciente(paciente: Paciente):
    """
    Simula el proceso de registro de un paciente.
    
    Parámetros:
    - paciente: Paciente que será registrado.
    """
    log_event(f"Registrando paciente: {paciente.nombre} (ID: {paciente.id})")
    # Simula el tiempo que toma registrar un paciente
    import time
    time.sleep(1 + paciente.prioridad * 0.5)  # El tiempo varía según la prioridad
    log_event(f"Paciente {paciente.nombre} registrado correctamente.")

def registrar_pacientes_concurrentemente(pacientes):
    """
    Registra múltiples pacientes concurrentemente usando hilos (threads).
    
    Parámetros:
    - pacientes: Lista de objetos Paciente.
    """
    threads = []
    for paciente in pacientes:
        t = threading.Thread(target=registrar_paciente, args=(paciente,))
        threads.append(t)
        t.start()

    # Espera a que todos los hilos terminen
    for t in threads:
        t.join()
