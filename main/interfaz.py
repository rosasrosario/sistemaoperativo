# Importamos las librerías necesarias para la interfaz gráfica y otras funcionalidades
import tkinter as tk
from tkinter import scrolledtext
import sys
from text_redirector import TextRedirector
from scheduling import Scheduling
from memoria import Memoria
from proceso import Proceso

# Definimos la clase Interfaz que manejará la GUI del simulador
class Interfaz:
    def __init__(self, procesos, quantum):
        # Inicializamos la ventana principal de la interfaz
        self.root = tk.Tk()
        self.root.title('Simulador de Sistema Operativo')
        self.root.configure(bg='#2b2b2b')  # Fondo oscuro

        # Creamos un canvas para dibujar la línea de tiempo y los procesos
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg='#1e1e1e', highlightthickness=0)
        self.canvas.pack(pady=10)

        # Convertimos la lista de procesos en instancias de la clase Proceso
        self.procesos = [Proceso(p.id_proceso, p.tiempo_llegada, p.tiempo_ejecucion) for p in procesos]
        self.quantum = quantum  # Quantum de tiempo para el algoritmo Round Robin

        # Botón para iniciar la ejecución de los procesos
        self.boton_iniciar = tk.Button(self.root, text="Iniciar Ejecución", command=self.iniciar_ejecucion, 
                                       bg='#007acc', fg='white', font=('Helvetica', 12, 'bold'), relief='flat')
        self.boton_iniciar.pack(pady=10)

        # Dibujamos la línea de tiempo en el canvas
        self.dibujar_linea_tiempo()

        # Widget de texto con scroll para mostrar la salida del simulador
        self.text_widget = scrolledtext.ScrolledText(self.root, width=100, height=10, bg='#1e1e1e', fg='white', 
                                                     insertbackground='white', font=('Courier', 10), relief='flat', bd=0)
        self.text_widget.pack(pady=10)

        # Redireccionamos stdout para mostrar la salida en el widget de texto
        self.text_redirector = TextRedirector(self.text_widget)
        sys.stdout = self.text_redirector

    # Método para dibujar la línea de tiempo
    def dibujar_linea_tiempo(self):
        self.canvas.create_line(50, 50, 750, 50, width=2, fill='white')
        for i in range(51, 751, 50):
            self.canvas.create_line(i, 50, i, 55, width=2, fill='white')

    # Método para dibujar un proceso en el canvas
    def dibujar_proceso(self, proceso, x_inicio, y_inicio):
        x_fin = x_inicio + proceso.tiempo_ejecucion * 10
        y_fin = y_inicio + 30
        self.canvas.create_rectangle(x_inicio, y_inicio, x_fin, y_fin, fill='skyblue', outline='#007acc')
        self.canvas.create_text((x_inicio + x_fin) / 2, (y_inicio + y_fin) / 2, text=f'P{proceso.id_proceso}', 
                                fill='white', font=('Helvetica', 10, 'bold'))
        print(f'Proceso {proceso.id_proceso} ejecutado de {x_inicio/10} a {x_fin/10}.')

    # Método para iniciar la ejecución de los procesos
    def iniciar_ejecucion(self):
        print("Ejecución de procesos:")
        # Creamos una instancia de Scheduling y ejecutamos el algoritmo Round Robin
        scheduler = Scheduling(self.procesos, self.quantum)
        eventos = scheduler.round_robin()

        # Dibujamos el gráfico de Gantt con los eventos obtenidos del scheduling
        self.dibujar_grafico_gantt(eventos)

        # Gestión de memoria
        print("\nGestión de memoria:")
        memoria = Memoria(20)  # Inicializamos la memoria con tamaño 20
        for proceso in self.procesos:
            memoria.agregar_proceso(proceso)  # Agregamos cada proceso a la memoria

        # Liberamos la memoria de un proceso específico
        memoria.liberar_memoria(self.procesos[1])

        # Mostramos información de los procesos y la memoria utilizada
        print("\nProcesos:")
        for proceso in self.procesos:
            memoria_utilizada = memoria.obtener_memoria_utilizada()
            print(f"Proceso {proceso.id_proceso}: Memoria utilizada = {memoria_utilizada}")
            print(proceso)

    # Método para dibujar el gráfico de Gantt
    def dibujar_grafico_gantt(self, eventos):
        y_inicio = 70
        altura_proceso = 30
        for evento in eventos:
            proceso, t_inicio, t_fin = evento
            x_inicio = 50 + t_inicio * 10
            x_fin = 50 + t_fin * 10
            y_fin = y_inicio + altura_proceso
            self.canvas.create_rectangle(x_inicio, y_inicio, x_fin, y_fin, fill='skyblue', outline='#007acc')
            self.canvas.create_text((x_inicio + x_fin) / 2, (y_inicio + y_fin) / 2, text=f'P{proceso.id_proceso}', 
                                    fill='white', font=('Helvetica', 10, 'bold'))
            y_inicio += altura_proceso + 10
