from sympy import symbols, lambdify, sympify, diff
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from grafica import GraficaInterfaz

class Cinematica:
    def __init__(self, ecu_posicion):
        self.t = symbols('t') #Variable independiente
        ecuacion_posicion = sympify(ecu_posicion)
        #Calcula la ecuacion de velocidad
        ecu_velocidad = diff(ecuacion_posicion, self.t)
        #Caula la ecuacion de aceleracion
        """Borre este comentario y coloque lo realizado en la linea anterior pero asignado a la ecuacion de aceleracion"""
        #Convierte las ecuaciones a funciones evaluables
        self.ecuacion_posicion = lambdify(self.t, ecuacion_posicion)
        self.ecuacion_velocidad = lambdify(self.t, ecu_velocidad)
        """Borre este comentario y coloque lo realizado en la linea anterior pero asignado a la ecuacion de aceleracion"""

    
    def calcular_posicion (self, tiempo):
        return self.ecuacion_posicion(tiempo)
    
    def calcular_velocidad (self, tiempo):
        pass

    def calcular_aceleracion (self, tiempo):
        pass

    def graficar_posicion (self, lim_inf, lim_sup):
        tiempo = np.linspace(lim_inf, lim_sup, 100)
        posicion = [self.ecuacion_posicion(t) for t in tiempo]
        plt.plot(tiempo, posicion)
        plt.title("Grafica de posicion")
        plt.xlabel("Tiempo (t)")
        plt.ylabel("Posicion (m)")
        plt.grid(True)
        plt.legend()
        plt.show()

    def graficar_velocidad():
        pass

    def graficar_aceleracion():
        pass
    

class CinematicaInterfaz:
    def __init__(self, ventana_principal = None, frame = None):
        #Si se manda una ventana principal MRU trabajara como ventana secundaria
        if ventana_principal is not None and frame is None:
            self.ventana = tk.Toplevel(ventana_principal)
        #Si se manda un frame, MRU se colocara dentro de ese frame
        elif frame is not None and ventana_principal is None:
            self.ventana = frame
        #En caso contrario trabajara como una ventana principal
        else:
            # Crear ventana principal
            self.ventana = tk.Tk()             # Se crea la ventana 
            self.ventana.title("Cinematica")     # Agregamos un titulo a la ventana
            self.ventana.geometry("900x400")   # Determinamos el tamñao

        self.entry_resultados = {}

        tk.Label(self.ventana, text="Cinematica").pack()

        frame_izquierdo = tk.Frame(self.ventana, width=200)
        frame_izquierdo.pack(side="left", fill="y")

        subframe_inferior = tk.Frame(frame_izquierdo, height=30, width=200)
        subframe_inferior.pack(side="bottom", fill="x",padx=5, pady=5)

        subframe_izquierdo = tk.Frame(frame_izquierdo, width=100)
        subframe_izquierdo.pack(side="left", fill="y",padx=5, pady=10)

        subframe_derecho = tk.Frame(frame_izquierdo, width=100)
        subframe_derecho.pack(side="right", fill="y", pady=10, padx=5)

        frame_derecho = tk.Frame(self.ventana, width=100)
        frame_derecho.pack(side="right", fill=tk.BOTH, expand=True)

        tk.Label(subframe_izquierdo, text="Ecuacion de Posicion").pack(padx=5, pady=5)
        self.entry_ecupos = tk.Entry(subframe_izquierdo)
        self.entry_ecupos.pack(padx=5, pady=5)

        tk.Label(subframe_izquierdo, text="Tiempo").pack(padx=5, pady=5)
        self.entry_tiempo = tk.Entry(subframe_izquierdo)
        self.entry_tiempo.pack(padx=5, pady=5)

        entry_posicion = tk.Entry(subframe_derecho)
        self.entry_resultados["Posicion"] = entry_posicion

        entry_velocidad = tk.Entry(subframe_derecho)
        self.entry_resultados["Velocidad"] = entry_velocidad

        entry_aceleracion = tk.Entry(subframe_derecho)
        self.entry_resultados["Aceleracion"] = entry_aceleracion

        for columna, entry in self.entry_resultados.items():
            tk.Label(subframe_derecho, text=columna).pack(padx=5, pady=5)
            entry.pack(padx=5, pady=5)
            entry.config(state="disabled")

        btn_calcular = tk.Button(subframe_inferior, text="Calcular",command=self.calcular)
        btn_calcular.pack(anchor="center")

        btn_graficas_pos = tk.Button(subframe_inferior, text="Grafica (x)", command=self.graficar_posicion)
        btn_graficas_pos.pack(side="left", pady=10, padx=10)

        btn_graficas_vel = tk.Button(subframe_inferior, text="Grafica (V)")
        btn_graficas_vel.pack(side="left", pady=10, padx=10)

        btn_graficas_acel = tk.Button(subframe_inferior, text="Grafica (A)")
        btn_graficas_acel.pack(side="left", pady=10, padx=10)

        self.grafica = GraficaInterfaz(frame_derecho)
        self.ventana.mainloop()
    
    def calcular(self):
        self.cinematica = Cinematica(self.entry_ecupos.get())
        for entry in self.entry_resultados.values():
            entry.config(state="normal")
            entry.delete(0, tk.END)

        self.entry_resultados["Posicion"].insert(0, str(
            self.cinematica.calcular_posicion(float(self.entry_tiempo.get()))))
        
        for entry in self.entry_resultados.values():
            entry.config(state="disabled")

    def graficar_posicion(self):
        self.cinematica = Cinematica(self.entry_ecupos.get())
        self.grafica.graficar_funcion(self.cinematica.ecuacion_posicion,10)




#CinematicaInterfaz()
#cin = Cinematica("t**2")
#print(cin.calcular_posicion(2))

