from proceso import Proceso

class Scheduling:
    def __init__(self, procesos, quantum):
        self.procesos = [Proceso(p.id_proceso, p.tiempo_llegada, p.tiempo_ejecucion) for p in procesos]
        self.quantum = quantum

    def round_robin(self):
        tiempo_actual = 0 
        cola_listos = self.procesos[:] 
        eventos = []  

        while cola_listos:
            proceso_actual = cola_listos.pop(0)  
            t_inicio = tiempo_actual  

            if proceso_actual.tiempo_ejecucion > self.quantum:
                tiempo_actual += self.quantum  
                proceso_actual.tiempo_ejecucion -= self.quantum  
                cola_listos.append(proceso_actual)  
            else:
                tiempo_actual += proceso_actual.tiempo_ejecucion 
                proceso_actual.tiempo_ejecucion = 0 

            t_fin = tiempo_actual 
            eventos.append((proceso_actual, t_inicio, t_fin))  
            print(f"Proceso {proceso_actual.id_proceso} ejecutado de {t_inicio} a {t_fin}")

        return eventos
