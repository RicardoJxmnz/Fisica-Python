# Importación de clases personalizadas
from vector import*                        # Importa todo desde el módulo vector (debe contener VectorPolar y VectorRectangular)
from calculadora_vector import*           # Importa todo desde calculadora_vector (debe contener CalculadoraVector)

# Importación de librerías para la interfaz gráfica y visualización
import tkinter as tk                      # Tkinter para GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Integración de matplotlib con tkinter
import matplotlib.pyplot as plt           # Para graficar
import numpy as np                        # Utilidades numéricas (no usada explícitamente aquí)

# Lista de vectores y colores para asignar uno a cada vector
vectores = []                             # Almacena los vectores creados
colores = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "white", "orange","purple",  
    "pink", "brown", "gray", "olive", "navy"]  # Lista de colores usados para distinguir vectores
calculadora = CalculadoraVector()         # Instancia de la clase que realiza operaciones vectoriales

# Función que crea un vector polar a partir de las entradas
def crear_polar():
    try:
        # Crea el vector polar usando los valores ingresados
        vector = VectorPolar(float(entrada1.get()), float(entrada2.get()))
        vectores.append(vector)           # Lo agrega a la lista
        actualizar_grafica()              # Refresca el gráfico

        # Desactiva las entradas si ya hay dos vectores
        if len(vectores) == 2:
            entrada1.config(state="disabled")
            entrada2.config(state="disabled")
    except Exception as e:
        print("Error al crear el vector:", e)

# Función para actualizar la gráfica con los vectores actuales
def actualizar_grafica():
    ax.clear()                            # Limpia el área de dibujo
    ax.axhline(0,color="black", lw=0.5)   # Dibuja el eje x
    ax.axvline(0,color="black", lw=0.5)   # Dibuja el eje y

    # Ajusta los límites dinámicamente basados en los vectores, centrados en 0
    ax.set_xlim(min(*[v.x for v in vectores], 0) - 1, max(*[v.x for v in vectores], 0) + 1)
    ax.set_ylim(min(*[v.y for v in vectores], 0) - 1, max(*[v.y for v in vectores], 0) + 1)
    ax.grid(True)                         # Activa el fondo cuadriculado
    ax.set_aspect('equal')               # Mantiene proporción 1:1 en la gráfica
    
    # Dibuja cada vector con su color y etiqueta
    for vector, color in zip(vectores, colores):
        plt.quiver(0, 0, vector.x, vector.y, angles="xy", scale_units="xy", 
                   scale=1, color=color, label=f"({vector.x:.2f}, {vector.y:.2f})")
    
    ax.legend()                           # Muestra la leyenda con etiquetas de vectores
    canvas.draw()                         # Refresca el lienzo en la interfaz

# Función para limpiar la gráfica y resetear todo
def limpiar_grafica():
    ax.clear()                            # Limpia la gráfica
    ax.axhline(0,color="black", lw=0.5)   # Redibuja el eje x
    ax.axvline(0,color="black", lw=0.5)   # Redibuja el eje y
    ax.set_xlim(-10, 10)                  # Restaura límites por defecto
    ax.set_ylim(-10, 10)
    ax.grid(True)
    canvas.draw()                         # Refresca la gráfica
    vectores.clear()                      # Elimina todos los vectores
    entrada1.config(state="normal")       # Habilita entradas nuevamente
    entrada2.config(state="normal")

# Función que suma los dos primeros vectores y actualiza la gráfica
def sumar_vector():
    x, y = calculadora.suma_vector(vectores[0], vectores[1])  # Suma de vectores
    vector = VectorRectangular(x, y)        # Crea el vector resultante como rectangular
    vectores.append(vector)                 # Lo agrega a la lista
    actualizar_grafica()                    # Actualiza gráfica

# --------- INTERFAZ GRÁFICA ------------

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Vectores")
ventana.geometry("600x500")

# Entradas de texto para coordenadas polares
tk.Label(ventana, text="(x o r):").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="(y o angulo):").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

# Botones de control
tk.Button(ventana, text="Crear Vector Polar", command=crear_polar).pack(pady=2)
tk.Button(ventana, text="Limpiar Grafica", command=limpiar_grafica).pack(pady=2)
tk.Button(ventana, text="Sumar Vectores", command=sumar_vector).pack(pady=2)

# Crear y configurar la figura de matplotlib
fig, ax = plt.subplots()
ax.axhline(0,color="black", lw=0.5)      # Eje x
ax.axvline(0,color="black", lw=0.5)      # Eje y
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True)
ax.set_xlabel("x")                       # Etiqueta del eje x
ax.set_ylabel("y")                       # Etiqueta del eje y
ax.set_aspect('equal')                  # Proporción 1:1

# Inserta la gráfica dentro de la ventana de Tkinter
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(pady=10, fill=tk.BOTH, expand=True)

# Inicia el bucle de la interfaz gráfica
ventana.mainloop()

# Cierra todas las ventanas de matplotlib al terminar
plt.close('all')
