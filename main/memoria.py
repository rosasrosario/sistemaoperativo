# Definimos la clase BloqueMemoria que representa un bloque de memoria en el sistema
class BloqueMemoria:
    def __init__(self, id_bloque, tamaño):
        self.id_bloque = id_bloque           # Identificador del bloque de memoria
        self.tamaño = tamaño                 # Tamaño del bloque de memoria
        self.proceso_asignado = None         # Proceso asignado al bloque, inicialmente ninguno

# Definimos la clase Memoria que gestiona los bloques de memoria y la asignación de procesos a la memoria
class Memoria:
    def __init__(self, tamaño_total):
        self.tamaño_total = tamaño_total     # Tamaño total de la memoria
        self.bloques = [BloqueMemoria(1, tamaño_total)]  # Inicialmente, un único bloque de memoria del tamaño total
        self.procesos_asignados = {}         # Diccionario para mantener un registro de los procesos asignados

    # Método para agregar un proceso a la memoria
    def agregar_proceso(self, proceso):
        if self.asignar_memoria(proceso):    # Intenta asignar memoria al proceso
            print(f'Proceso {proceso.id_proceso} agregado y asignado a la memoria.')
            self.procesos_asignados[proceso.id_proceso] = proceso.tiempo_ejecucion  # Registro del proceso asignado
        else:
            print(f'Proceso {proceso.id_proceso} no se pudo agregar por falta de memoria.')

    # Método para asignar memoria a un proceso
    def asignar_memoria(self, proceso):
        for bloque in self.bloques:  # Recorre todos los bloques de memoria
            # Si el bloque no tiene un proceso asignado y su tamaño es suficiente para el proceso
            if not bloque.proceso_asignado and bloque.tamaño >= proceso.tiempo_ejecucion:
                bloque.proceso_asignado = proceso  # Asigna el proceso al bloque
                tamaño_restante = bloque.tamaño - proceso.tiempo_ejecucion
                bloque.tamaño = proceso.tiempo_ejecucion  # Ajusta el tamaño del bloque al del proceso

                # Si queda espacio en el bloque, crea un nuevo bloque con el tamaño restante
                if tamaño_restante > 0:
                    nuevo_bloque = BloqueMemoria(len(self.bloques) + 1, tamaño_restante)
                    self.bloques.append(nuevo_bloque)
                
                return True  # La asignación fue exitosa
        return False  # No se encontró un bloque suficiente para el proceso

    # Método para liberar la memoria ocupada por un proceso
    def liberar_memoria(self, proceso):
        for bloque in self.bloques:  # Recorre todos los bloques de memoria
            if bloque.proceso_asignado == proceso:  # Encuentra el bloque asignado al proceso
                bloque.proceso_asignado = None  # Libera el bloque
                bloque.tamaño += proceso.tiempo_ejecucion  # Devuelve el tamaño del proceso al bloque
                del self.procesos_asignados[proceso.id_proceso]  # Elimina el proceso del registro
                return True  # La liberación fue exitosa
        return False  # No se encontró el proceso en los bloques

    # Método para obtener la memoria utilizada
    def obtener_memoria_utilizada(self):
        memoria_utilizada = sum(self.procesos_asignados.values())  # Suma los tamaños de todos los procesos asignados
        return memoria_utilizada  # Retorna la memoria utilizada
