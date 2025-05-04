# diagnostico.py

import asyncio
from logger import log_event
from datos_paciente import Paciente

async def diagnosticar_paciente(paciente: Paciente):
    """
    Simula un diagnóstico automatizado para el paciente usando IA (mockeada).

    Parámetros:
    - paciente: Paciente, el paciente que será diagnosticado.

    Retorna:
    - str, resultado del diagnóstico.
    """
    log_event(f"Iniciando diagnóstico para {paciente.nombre} (ID: {paciente.id})")
    
    # Simula una latencia como si se consultara un modelo de IA
    await asyncio.sleep(2.5)  # Latencia simulada
    
    # Diagnóstico falso basado en síntomas (simplificado)
    diagnostico = f"{paciente.sintomas} detectado. Requiere {'urgencia' if paciente.prioridad == 1 else 'observación'}."
    
    log_event(f"Diagnóstico completado para {paciente.nombre}: {diagnostico}")
    return diagnostico

async def diagnosticar_multiples_pacientes(pacientes):
    """
    Ejecuta diagnósticos simultáneos (asíncronos) para múltiples pacientes.

    Parámetros:
    - pacientes: lista de objetos Paciente.

    Retorna:
    - lista de diagnósticos en el mismo orden que los pacientes.
    """
    tareas = [diagnosticar_paciente(p) for p in pacientes]
    return await asyncio.gather(*tareas)
