class Proceso:
    def __init__(self, id_proceso, tiempo_llegada, tiempo_ejecucion):
        self.id_proceso = id_proceso  
        self.tiempo_llegada = tiempo_llegada  
        self.tiempo_ejecucion = tiempo_ejecucion 
        self.tiempo_espera = 0  
        self.tiempo_respuesta = -1  

    def __str__(self):
        return f"Proceso {self.id_proceso}: Llegada = {self.tiempo_llegada}, Ejecución = {self.tiempo_ejecucion}"
