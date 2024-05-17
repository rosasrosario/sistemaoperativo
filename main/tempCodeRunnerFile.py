# Crear procesos
proceso1 = Proceso(1, 0, 10)  # Crear instancia de Proceso
proceso2 = Proceso(2, 2, 5)  # Crear instancia de Proceso
proceso3 = Proceso(3, 4, 7)  # Crear instancia de Proceso

procesos = [proceso1, proceso2, proceso3]  # Lista de procesos
quantum = 3  # Valor del quantum

# Iniciar la interfaz gráfica
if __name__ == "__main__":
    memoria = Memoria(99)  # Especificar la memoria total disponible (por ejemplo, 20 unidades)
    
    # Intentar asignar memoria a los procesos
    for proceso in procesos:
        memoria.agregar_proceso(proceso)

    # Mostrar memoria ocupada y libre
    print(f"Memoria utilizada: {memoria.obtener_memoria_utilizada()}")
    print(f"Memoria libre: {memoria.tamaño_total - memoria.obtener_memoria_utilizada()}")