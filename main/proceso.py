# Definimos la clase Proceso que representa un proceso en el sistema operativo
class Proceso:
    def __init__(self, id_proceso, tiempo_llegada, tiempo_ejecucion):
        self.id_proceso = id_proceso  # Identificador único del proceso
        self.tiempo_llegada = tiempo_llegada  # Tiempo en el que el proceso llega al sistema
        self.tiempo_ejecucion = tiempo_ejecucion  # Tiempo que el proceso necesita para ejecutarse
        self.tiempo_espera = 0  # Tiempo que el proceso ha esperado en la cola, inicialmente 0
        self.tiempo_respuesta = -1  # Tiempo de respuesta del proceso, inicialmente -1 para indicar que no ha sido calculado

    # Método para representar el objeto Proceso como una cadena de texto
    def __str__(self):
        return f"Proceso {self.id_proceso}: Llegada = {self.tiempo_llegada}, Ejecución = {self.tiempo_ejecucion}"
