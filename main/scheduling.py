# Importamos la clase Proceso desde el módulo correspondiente
from proceso import Proceso

# Definimos la clase Scheduling que manejará la planificación de procesos
class Scheduling:
    def __init__(self, procesos, quantum):
        # Creamos una lista de procesos a partir de las instancias de la clase Proceso
        self.procesos = [Proceso(p.id_proceso, p.tiempo_llegada, p.tiempo_ejecucion) for p in procesos]
        self.quantum = quantum  # Definimos el quantum de tiempo para el algoritmo Round Robin

    # Método que implementa el algoritmo de planificación Round Robin
    def round_robin(self):
        tiempo_actual = 0  # Variable para llevar el tiempo actual del sistema
        cola_listos = self.procesos[:]  # Creamos una copia de la lista de procesos como cola de listos
        eventos = []  # Lista para almacenar los eventos de ejecución de los procesos

        # Bucle que se ejecuta mientras haya procesos en la cola de listos
        while cola_listos:
            # Obtenemos el primer proceso de la cola de listos
            proceso_actual = cola_listos.pop(0)
            t_inicio = tiempo_actual  # Guardamos el tiempo de inicio de la ejecución del proceso

            # Si el tiempo de ejecución del proceso es mayor que el quantum
            if proceso_actual.tiempo_ejecucion > self.quantum:
                tiempo_actual += self.quantum  # Incrementamos el tiempo actual en el valor del quantum
                proceso_actual.tiempo_ejecucion -= self.quantum  # Reducimos el tiempo de ejecución restante del proceso
                cola_listos.append(proceso_actual)  # Añadimos el proceso de nuevo al final de la cola de listos
            else:
                tiempo_actual += proceso_actual.tiempo_ejecucion  # Incrementamos el tiempo actual en el tiempo de ejecución restante del proceso
                proceso_actual.tiempo_ejecucion = 0  # Marcamos el proceso como completado

            t_fin = tiempo_actual  # Guardamos el tiempo de finalización de la ejecución del proceso
            eventos.append((proceso_actual, t_inicio, t_fin))  # Añadimos el evento de ejecución a la lista de eventos
            print(f"Proceso {proceso_actual.id_proceso} ejecutado de {t_inicio} a {t_fin}")

        return eventos  # Devolvemos la lista de eventos de ejecución
