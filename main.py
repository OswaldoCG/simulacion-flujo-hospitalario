# main.py

import asyncio
import threading
from datos_paciente import generar_pacientes
from registro import registrar_pacientes_concurrentemente
from diagnostico import diagnosticar_multiples_pacientes
from modelo_diagnostico import evaluar_modelo_en_paralelo
from recursos import asignar_recursos
from seguimiento import iniciar_seguimiento_concurrente
from logger import log_event

def asignar_recursos_concurrentemente(pacientes):
    """
    Ejecuta la asignación de recursos en múltiples hilos (concurrencia).
    """
    threads = []
    for paciente in pacientes:
        t = threading.Thread(target=asignar_recursos, args=(paciente,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

async def flujo_hospitalario():
    """
    Ejecuta todo el flujo de atención hospitalaria usando múltiples paradigmas.
    """
    log_event("Sistema hospitalario iniciado.")
    
    # 1. Generar pacientes simulados
    pacientes = generar_pacientes(num=5)

    # 2. Registrar pacientes (concurrentemente)
    registrar_pacientes_concurrentemente(pacientes)

    # 3. Diagnóstico automatizado (asíncrono)
    diagnósticos = await diagnosticar_multiples_pacientes(pacientes)
    for d in diagnósticos:
        log_event(f"Resultado IA: {d}")

    # 4. Evaluación intensiva del modelo (paralelo)
    resultados_ia = evaluar_modelo_en_paralelo(pacientes)
    for res in resultados_ia:
        log_event(f"Evaluación IA completada: {res}")

    # 5. Asignar recursos (concurrente con semáforos)
    asignar_recursos_concurrentemente(pacientes)

    # 6. Seguimiento clínico (concurrente)
    iniciar_seguimiento_concurrente(pacientes)

    log_event("Todos los pacientes han sido dados de alta. Sistema finalizado.")

if __name__ == "__main__":
    asyncio.run(flujo_hospitalario())
