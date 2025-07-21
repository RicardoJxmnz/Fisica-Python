from vector import*
from calculadora_vector import*
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Lista para almacenar los vectores creados
vectores = []
colores = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "white", "orange","purple",  
    "pink", "brown", "gray", "olive", "navy"]
calculadora = CalculadoraVector()

def crear_polar():
    try:
        vector = VectorPolar(float(entrada1.get()), float(entrada2.get()))
        vectores.append(vector)
        actualizar_grafica()
        if len(vectores) == 2:
            entrada1.config(state="disabled")
            entrada2.config(state="disabled")
    except Exception as e:
        print("Error al crear el vector:", e)

def crear_rectangular():
    try: 
        vector = VectorRectangular(float(entrada1.get()), float(entrada2.get()))
        vectores.append(vector)
        actualizar_grafica()
        if len(vectores) == 2:
            entrada1.config(state="disabled")
            entrada2.config(state="disabled")
    except Exception as e:
        print("Error al crear el vector:", e)

def actualizar_grafica():
    ax.clear()
    ax.axhline(0,color="black", lw=0.5)
    ax.axvline(0,color="black", lw=0.5)
    ax.set_xlim(min(*[v.x for v in vectores], 0) - 1, max(*[v.x for v in vectores], 0) + 1)
    ax.set_ylim(min(*[v.y for v in vectores], 0) - 1, max(*[v.y for v in vectores], 0) + 1)
    ax.grid(True)
    ax.set_aspect('equal')
    
    for vector, color in zip(vectores, colores):
        plt.quiver(0, 0, vector.x, vector.y, angles="xy", scale_units="xy", 
                   scale=1, color=color, label=f"({vector.x:.2f}, {vector.y:.2f})")
    ax.legend()
    canvas.draw()

def limpiar_grafica():
    ax.clear()
    ax.axhline(0,color="black", lw=0.5)
    ax.axvline(0,color="black", lw=0.5)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)
    canvas.draw()    
    vectores.clear()
    entrada1.config(state="normal")
    entrada2.config(state="normal")

def sumar_vector():
    x, y = calculadora.suma_vector(vectores[0], vectores[1])
    vector = VectorRectangular(x, y)
    vectores.append(vector)
    actualizar_grafica()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Vectores")
ventana.geometry("600x500")

# Entradas de texto
tk.Label(ventana, text="(x o r):").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="(y o angulo):").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Crear Vector Polar", command=crear_polar).pack(pady=2)
tk.Button(ventana, text="Crear Vector Rectangular", command=crear_rectangular).pack(pady=2)
tk.Button(ventana, text="Limpiar Grafica", command=limpiar_grafica).pack(pady=2)
tk.Button(ventana, text="Sumar Vectores", command=sumar_vector).pack(pady=2)

# Crear figura de matplotlib
fig, ax = plt.subplots()
ax.axhline(0,color="black", lw=0.5)
ax.axvline(0,color="black", lw=0.5)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_aspect('equal')

canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(pady=10, fill=tk.BOTH, expand=True)

ventana.mainloop()
plt.close('all')