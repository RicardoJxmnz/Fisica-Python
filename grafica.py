from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt   
import tkinter as tk
from vector import *

class GraficaInterfaz():
    colores = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "white", "orange","purple",  
    "pink", "brown", "gray", "olive", "navy"]

    def __init__(self, ventana):
        # Crear y configurar la figura de matplotlib
        self.fig, self.ax = plt.subplots()         # Se crea una figura y un eje
        self.ax.axhline(0, color="black", lw=0.5)  # Dibuja el eje X
        self.ax.axvline(0, color="black", lw=0.5)  # Dibuja el eje Y
        self.ax.set_xlim(-10, 10)                  # Límite horizontal
        self.ax.set_ylim(-10, 10)                  # Límite vertical
        self.ax.grid(True)                         # Muestra la cuadrícula
        self.ax.set_xlabel("x")                    # Etiqueta del eje x
        self.ax.set_ylabel("y")                    # Etiqueta del eje y
        self.ax.set_aspect('equal')                # Mantiene proporción 1:1 en la gráfica

        # Inserta la gráfica de matplotlib dentro de la ventana de Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=ventana)        # Se vincula la figura a Tkinter
        self.canvas.get_tk_widget().pack(pady=10, fill=tk.BOTH, expand=True)  # Se empaqueta y permite expandirse

    def actualizar_grafica(self, vectores):
        self.ax.clear()                            # Limpia el área de dibujo
        self.ax.axhline(0,color="black", lw=0.5)   # Dibuja el eje x
        self.ax.axvline(0,color="black", lw=0.5)   # Dibuja el eje y

        """Se agrega una exepcion para evitar generar errores si es que se llama a esta funcion y la lista de vectores esta vacia
        esto puede ocurrir cuando se van eliminando vectores individualmente. Y si la lista se queda sin vectores se pueden generar errores en 
        self.ax.set_xlim(min(*[v.x for v in self.vectores], 0) - 1, max(*[v.x for v in self.vectores], 0) + 1),"""
        try:
            # Ajusta los límites dinámicamente basados en los vectores
            """Para los limite inferior del eje x se determina cual es el valor minimo con respecto a todos 
            los vectores ingresados y se le resta 1 para mejor visualizacion los mismo para el limite superior, pero en este caso
            se suma 1"""
            self.ax.set_xlim(min(*[v.x for v in vectores], 0) - 1, max(*[v.x for v in vectores], 0) + 1)  #Limite inferior y superior del eje x 
            #Para el eje y se realiza lo mismo que en el eje x
            self.ax.set_ylim(min(*[v.y for v in vectores], 0) - 1, max(*[v.y for v in vectores], 0) + 1)  #limite inferior y superior del eje y
            self.ax.grid(True)             # Activa el fondo cuadriculado
            self.ax.set_aspect('equal')    # Mantiene proporción 1:1 en la gráfica

            # Dibuja cada vector con su color y etiqueta
            for vector, color in zip(vectores, GraficaInterfaz.colores):
                plt.quiver(0, 0, vector.x, vector.y, angles="xy", scale_units="xy",
                       scale=1, color=color, label=f"({vector.r:.2f}, {vector.angulo:.2f})")
            
            self.ax.legend()      # Muestra la leyenda con etiquetas de vectores
            self.canvas.draw()    # Refresca el lienzo en la interfaz
        except:
            self.limpiar_grafica()

    def limpiar_grafica(self):
        self.ax.clear()                            # Limpia la gráfica
        self.ax.axhline(0,color="black", lw=0.5)   # Redibuja el eje x
        self.ax.axvline(0,color="black", lw=0.5)   # Redibuja el eje y
        self.ax.set_xlim(-10, 10)                  # Restaura límites por defecto del eje x
        self.ax.set_ylim(-10, 10)                  # Restaura límites por defecto del eje y
        self.ax.grid(True)                         # Activa la cuadricula
        self.canvas.draw()                         # Refresca la gráfica