from sympy import symbols, lambdify, sympify, diff
import matplotlib.pyplot as plt
import numpy as np

class Cinematica:
    def __init__(self, ecu_posicion):
        self.t = symbols('t') #Variable independiente
        self.ecuacion_posicion = sympify(ecu_posicion)
        #Calcula la ecuacion de velocidad
        ecu_velocidad = diff(self.ecuacion_posicion, self.t)
        #Caula la ecuacion de aceleracion
        """Borre este comentario y coloque lo realizado en la linea anterior pero asignado a la ecuacion de aceleracion"""
        #Convierte las ecuaciones a funciones evaluables
        self.ecuacion_posicion = lambdify(self.t, self.ecuacion_posicion)
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
    
cinematica = Cinematica("3*t")
print(cinematica.calcular_posicion(2))
cinematica.graficar_posicion(0,10)