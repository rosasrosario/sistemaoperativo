class BloqueMemoria:
    def __init__(self, id_bloque, tamaño):
        self.id_bloque = id_bloque
        self.tamaño = tamaño
        self.proceso_asignado = None

class Memoria:
    def __init__(self, tamaño_total):
        self.tamaño_total = tamaño_total
        self.bloques = [BloqueMemoria(1, tamaño_total)]
        self.procesos_asignados = {}

    def agregar_proceso(self, proceso):
        if self.asignar_memoria(proceso):
            print(f'Proceso {proceso.id_proceso} agregado y asignado a la memoria.')
            self.procesos_asignados[proceso.id_proceso] = proceso.tiempo_ejecucion
        else:
            print(f'Proceso {proceso.id_proceso} no se pudo agregar por falta de memoria.')

    def asignar_memoria(self, proceso):
        for bloque in self.bloques:
            if not bloque.proceso_asignado and bloque.tamaño >= proceso.tiempo_ejecucion:
                bloque.proceso_asignado = proceso
                tamaño_restante = bloque.tamaño - proceso.tiempo_ejecucion
                bloque.tamaño = proceso.tiempo_ejecucion
                
                if tamaño_restante > 0:
                    nuevo_bloque = BloqueMemoria(len(self.bloques) + 1, tamaño_restante)
                    self.bloques.append(nuevo_bloque)
                
                return True
        return False

    def liberar_memoria(self, proceso):
        for bloque in self.bloques:
            if bloque.proceso_asignado == proceso:
                bloque.proceso_asignado = None
                bloque.tamaño += proceso.tiempo_ejecucion  # Devuelve el tamaño del proceso al bloque
                del self.procesos_asignados[proceso.id_proceso]
                return True
        return False

    def obtener_memoria_utilizada(self):
        memoria_utilizada = sum(self.procesos_asignados.values())
        return memoria_utilizada
