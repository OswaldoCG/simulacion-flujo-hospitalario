# simulacion-flujo-hospitalario
Simulación del flujo de pacientes en un hospital usando concurrencia y paralelismo en Python
# Sistema de Simulación de Flujo Hospitalario

Este sistema simula el flujo de pacientes a través de un hospital, demostrando el uso de concurrencia (hilos y asincronía) y paralelismo para optimizar la atención al paciente.

## Propósito

El propósito principal de esta simulación es ilustrar cómo diferentes técnicas de programación concurrente y paralela pueden aplicarse en un entorno hospitalario para mejorar la eficiencia en procesos como el registro de pacientes, el diagnóstico, la asignación de recursos y el seguimiento.

## Características Clave

* **Generación de Pacientes:** Simula la llegada de pacientes con diferentes atributos (nombre, prioridad, síntomas).
* **Registro de Pacientes:** Registra a los pacientes de forma concurrente, simulando la atención de múltiples pacientes en paralelo.
* **Diagnóstico Automatizado:** Simula un diagnóstico rápido mediante IA (mockeado) utilizando programación asíncrona para no bloquear el flujo principal.
* **Evaluación de Modelo de IA:** Ejecuta una evaluación intensiva del diagnóstico de IA en paralelo para múltiples pacientes.
* **Asignación de Recursos:** Asigna recursos limitados (camas y doctores) a los pacientes utilizando semáforos para evitar la sobreasignación.
* **Seguimiento Clínico:** Realiza un seguimiento de los pacientes después del diagnóstico y antes del alta, utilizando concurrencia.
* **Registro de Eventos:** Utiliza un sistema de logging para registrar eventos importantes del sistema.
* **Benchmark:** Permite medir el rendimiento de la simulación.

## Requisitos

* Python 3.10.11

## Dependencias

El proyecto utiliza las siguientes bibliotecas de Python estándar:

* `asyncio`:  Para programación asíncrona.
* `threading`:  Para programación concurrente con hilos.
* `logging`:  Para registrar eventos del sistema.
* `random`:   Para generar datos aleatorios (nombres, síntomas, prioridades).
* `time`:     Para simular tiempos de espera.
* `multiprocessing`: Para programación paralela.
* `os`:       Para operaciones del sistema de archivos (creación de directorios de logs).
* `datetime`: Para generar nombres de archivos de log basados en la fecha y hora.

## Instalación

1.  Clona el repositorio:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```

2.  (Opcional pero recomendado) Crea un entorno virtual:

    ```bash
    python -m venv venv
    ```

3.  Activa el entorno virtual:

    * En Windows:

        ```bash
        venv\Scripts\activate
        ```

    * En Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

4.  Ejecuta el programa principal:

    ```bash
    python main.py
    ```

## Estructura del Código

* `main.py`:  Ejecuta el flujo principal de la simulación del sistema hospitalario, coordinando la generación de pacientes, registro, diagnóstico, asignación de recursos y seguimiento.
* `datos_paciente.py`: Define la clase `Paciente` y la función `generar_pacientes` para crear objetos que representan a los pacientes en la simulación.
* `registro.py`:  Contiene las funciones `registrar_paciente` y `registrar_pacientes_concurrentemente` para simular el proceso de registro de pacientes, utilizando hilos para la concurrencia.
* `diagnostico.py`:  Incluye las funciones `diagnosticar_paciente` y `diagnosticar_multiples_pacientes` para simular el diagnóstico de pacientes, empleando asincronía para manejar múltiples diagnósticos simultáneamente.
* `modelo_diagnostico.py`:  Define las funciones `modelo_ia_simulado` y `evaluar_modelo_en_paralelo` para simular un modelo de IA de diagnóstico y su evaluación paralela usando `multiprocessing`.
* `recursos.py`:  Gestiona la asignación de recursos (camas y doctores) a los pacientes mediante semáforos, con la función `asignar_recursos`.
* `seguimiento.py`:  Contiene las funciones `seguimiento_paciente` e `iniciar_seguimiento_concurrente` para simular el seguimiento clínico de los pacientes, utilizando hilos para la concurrencia.
* `logger.py`:  Configura el sistema de logging para registrar eventos del sistema en archivos y en la consola, con la función `log_event`.
* `benchmark.py`:  Contiene las funciones para medir el rendimiento de la simulación, específicamente `medir_rendimiento`.

## Ejecutar el Benchmark

Para medir el rendimiento de la simulación, puedes ejecutar el script `benchmark.py`. Este script mide el tiempo que tarda en ejecutarse la simulación con un número determinado de pacientes.

```bash
python benchmark.py
