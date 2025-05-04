# modelo_diagnostico.py

import time
import random
from multiprocessing import Pool, cpu_count
from datos_paciente import Paciente

def modelo_ia_simulado(paciente: Paciente):
    """
    Simula un modelo de IA realizando un análisis pesado del paciente.

    Parámetros:
    - paciente: Paciente, el paciente a analizar.

    Retorna:
    - dict con resultado de análisis.
    """
    # Simulación de cómputo intensivo
    tiempo_procesamiento = random.uniform(1.5, 3.5)
    time.sleep(tiempo_procesamiento)

    resultado = {
        "id": paciente.id,
        "nombre": paciente.nombre,
        "riesgo": random.choice(["bajo", "medio", "alto"]),
        "tiempo": round(tiempo_procesamiento, 2)
    }

    return resultado

def evaluar_modelo_en_paralelo(pacientes):
    """
    Ejecuta análisis del modelo IA en paralelo para una lista de pacientes.

    Parámetros:
    - pacientes: lista de objetos Paciente.

    Retorna:
    - lista de dicts con resultados.
    """
    with Pool(cpu_count()) as pool:
        resultados = pool.map(modelo_ia_simulado, pacientes)
    return resultados
