# Importamos las librerías necesarias para la interfaz gráfica y otras funcionalidades
import tkinter as tk
from tkinter import scrolledtext
import sys

# Importamos las clases necesarias de archivos externos
from text_redirector import TextRedirector
from scheduling import Scheduling
from memoria import Memoria
from proceso import Proceso
from interfaz import Interfaz

# Crear instancias de procesos con id, tiempo de llegada y tiempo de ejecución
proceso1 = Proceso(1, 0, 10)  # Proceso 1 llega en el tiempo 0 y tiene un tiempo de ejecución de 10 unidades
proceso2 = Proceso(2, 2, 5)   # Proceso 2 llega en el tiempo 2 y tiene un tiempo de ejecución de 5 unidades
proceso3 = Proceso(3, 4, 7)   # Proceso 3 llega en el tiempo 4 y tiene un tiempo de ejecución de 7 unidades

# Guardamos los procesos en una lista
procesos = [proceso1, proceso2, proceso3]

# Definimos el quantum de tiempo para el algoritmo Round Robin
quantum = 3

# Comprobamos si el script se está ejecutando como el programa principal
if __name__ == "__main__":
    # Creamos una instancia de Memoria con tamaño 15
    memoria = Memoria(15)
    
    # Asignamos memoria a cada uno de los procesos
    for proceso in procesos:
        memoria.agregar_proceso(proceso)

    # Mostramos la memoria utilizada y la memoria libre en la consola
    print(f"Memoria utilizada: {memoria.obtener_memoria_utilizada()}")
    print(f"Memoria libre: {memoria.tamaño_total - memoria.obtener_memoria_utilizada()}")

    # Creamos una instancia de la clase Interfaz, pasándole los procesos y el quantum
    interfaz = Interfaz(procesos, quantum)
    
    # Iniciamos el bucle principal de la interfaz gráfica
    interfaz.root.mainloop()
