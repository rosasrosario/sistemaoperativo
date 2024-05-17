import tkinter as tk
from tkinter import scrolledtext
import sys
from text_redirector import TextRedirector
from scheduling import Scheduling
from memoria import Memoria
from proceso import Proceso

class Interfaz:
    def __init__(self, procesos, quantum):
        self.root = tk.Tk()
        self.root.title('Simulador de Sistema Operativo')
        self.root.configure(bg='#2b2b2b')

        self.canvas = tk.Canvas(self.root, width=800, height=400, bg='#1e1e1e', highlightthickness=0)
        self.canvas.pack(pady=10)

        self.procesos = [Proceso(p.id_proceso, p.tiempo_llegada, p.tiempo_ejecucion) for p in procesos]
        self.quantum = quantum

        self.boton_iniciar = tk.Button(self.root, text="Iniciar Ejecución", command=self.iniciar_ejecucion, 
                                       bg='#007acc', fg='white', font=('Helvetica', 12, 'bold'), relief='flat')
        self.boton_iniciar.pack(pady=10)

        self.dibujar_linea_tiempo()

        self.text_widget = scrolledtext.ScrolledText(self.root, width=100, height=10, bg='#1e1e1e', fg='white', 
                                                     insertbackground='white', font=('Courier', 10), relief='flat', bd=0)
        self.text_widget.pack(pady=10)

        self.text_redirector = TextRedirector(self.text_widget)
        sys.stdout = self.text_redirector

    def dibujar_linea_tiempo(self):
        self.canvas.create_line(50, 50, 750, 50, width=2, fill='white')
        for i in range(51, 751, 50):
            self.canvas.create_line(i, 50, i, 55, width=2, fill='white')

    def dibujar_proceso(self, proceso, x_inicio, y_inicio):
        x_fin = x_inicio + proceso.tiempo_ejecucion * 10
        y_fin = y_inicio + 30
        self.canvas.create_rectangle(x_inicio, y_inicio, x_fin, y_fin, fill='skyblue', outline='#007acc')
        self.canvas.create_text((x_inicio + x_fin) / 2, (y_inicio + y_fin) / 2, text=f'P{proceso.id_proceso}', 
                                fill='white', font=('Helvetica', 10, 'bold'))
        print(f'Proceso {proceso.id_proceso} ejecutado de {x_inicio/10} a {x_fin/10}.')

    def iniciar_ejecucion(self):
        print("Ejecución de procesos:")
        scheduler = Scheduling(self.procesos, self.quantum)
        eventos = scheduler.round_robin()

        self.dibujar_grafico_gantt(eventos)

        print("\nGestión de memoria:")
        memoria = Memoria(20)
        for proceso in self.procesos:
            memoria.agregar_proceso(proceso)

        memoria.liberar_memoria(self.procesos[1])

        print("\nProcesos:")
        for proceso in self.procesos:
            memoria_utilizada = memoria.obtener_memoria_utilizada()
            print(f"Proceso {proceso.id_proceso}: Memoria utilizada = {memoria_utilizada}")
            print(proceso)

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
