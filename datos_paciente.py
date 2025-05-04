# datos_paciente.py

import random

class Paciente:
    def __init__(self, id, nombre, prioridad, sintomas):
        self.id = id
        self.nombre = nombre
        self.prioridad = prioridad
        self.sintomas = sintomas

def generar_pacientes(num=5):
    """
    Genera una lista de pacientes simulados.

    Parámetros:
    - num: número de pacientes a generar.

    Retorna:
    - lista de objetos Paciente.
    """
    nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis"]
    sintomas_posibles = ["dolor de cabeza", "fiebre", "tos", "dolor abdominal", "dificultad respiratoria"]

    pacientes = []
    for i in range(num):
        paciente = Paciente(
            id=i + 1,
            nombre=random.choice(nombres),
            prioridad=random.randint(1, 3),  # Prioridad 1: alta, 2: media, 3: baja
            sintomas=random.choice(sintomas_posibles)
        )
        pacientes.append(paciente)
    
    return pacientes
