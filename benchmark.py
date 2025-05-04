import time
import asyncio
from logger import logger

async def medir_rendimiento(num_pacientes, main_function):
    """Mide el tiempo de ejecución de la simulación."""
    inicio = time.time()
    await main_function(num_pacientes)
    fin = time.time()
    duracion = fin - inicio
    logger.info(f"Simulación con {num_pacientes} pacientes completada en {duracion:.2f} segundos.")
    return duracion

# Ejemplo de cómo se podría usar en main.py
async def main_con_medicion(num_pacientes):
    # Aquí iría la lógica principal de tu simulación, similar a main.py
    # pero estructurada para ser llamada por medir_rendimiento
    from main import main as simulacion_main
    await simulacion_main(num_pacientes)

if __name__ == '__main__':
    async def test_benchmark():
        await medir_rendimiento(5, main_con_medicion)

    asyncio.run(test_benchmark())