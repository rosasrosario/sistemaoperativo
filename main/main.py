import tkinter as tk
from tkinter import scrolledtext
import sys
from text_redirector import TextRedirector
from scheduling import Scheduling
from memoria import Memoria
from proceso import Proceso
from interfaz import Interfaz


# Crear procesos
proceso1 = Proceso(1, 0, 10) 
proceso2 = Proceso(2, 2, 5)  
proceso3 = Proceso(3, 4, 7)  
procesos = [proceso1, proceso2, proceso3] 
quantum = 3  

# Iniciar la interfaz gráfica
if __name__ == "__main__":
    memoria = Memoria(15) 
    
    for proceso in procesos:  # Asignar memoria a los procesos
        memoria.agregar_proceso(proceso)

    # Mostrar memoria ocupada y libre
    print(f"Memoria utilizada: {memoria.obtener_memoria_utilizada()}")
    print(f"Memoria libre: {memoria.tamaño_total - memoria.obtener_memoria_utilizada()}")

    interfaz = Interfaz(procesos, quantum)  
    interfaz.root.mainloop()  
