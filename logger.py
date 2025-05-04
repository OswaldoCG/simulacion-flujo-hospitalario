# logger.py
import logging
import os
from datetime import datetime

# Creamos un directorio para logs si no existe
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Nombre del archivo de log basado en la fecha actual
log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
log_path = os.path.join(log_dir, log_filename)

# Configuramos el logger principal del sistema
logging.basicConfig(
    level=logging.DEBUG,  # Nivel de detalle (DEBUG para desarrollo)
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path),  # Guarda en archivo
        logging.StreamHandler()         # También imprime en consola
    ]
)

# Función simple para registrar eventos
def log_event(message, level="info"):
    """
    Registra un evento en el sistema hospitalario.
    
    Parámetros:
    - message: str, el mensaje a registrar.
    - level: str, el nivel del log (info, warning, error, debug).
    """
    if level == "debug":
        logging.debug(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.info(message)
