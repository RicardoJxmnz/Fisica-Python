from sympy import symbols, lambdify, sympify, diff
import matplotlib.pyplot as plt
import numpy as np

class Movimiento:
    def __init__(self, expresion_str):
        self.t = symbols('t')  # Variable simbólica
        self.exp_pos = sympify(expresion_str)  # Ecuación de posición simbólica

        # Derivadas
        self.exp_vel = diff(self.exp_pos, self.t)
        self.exp_acel = diff(self.exp_vel, self.t)

        # Funciones numéricas evaluables
        self.f_pos = lambdify(self.t, self.exp_pos, modules='math')
        self.f_vel = lambdify(self.t, self.exp_vel, modules='math')
        self.f_acel = lambdify(self.t, self.exp_acel, modules='math')

    def posicion(self, t_val):
        return self.f_pos(t_val)

    def velocidad(self, t_val):
        return self.f_vel(t_val)

    def aceleracion(self, t_val):
        return self.f_acel(t_val)

    def mostrar_ecuaciones(self):
        return {
            "posición": f"x(t) = {self.exp_pos}",
            "velocidad": f"v(t) = {self.exp_vel}",
            "aceleración": f"a(t) = {self.exp_acel}"
        }

    def graficar_posicion(self, t_min, t_max, puntos=100):
        t_vals = np.linspace(t_min, t_max, puntos)
        y_vals = [self.f_pos(t) for t in t_vals]
        plt.plot(t_vals, y_vals, label='x(t)', color='blue')
        plt.title("Gráfica de posición")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Posición (m)")
        plt.grid(True)
        plt.legend()
        plt.show()

    def graficar_velocidad(self, t_min, t_max, puntos=100):
        t_vals = np.linspace(t_min, t_max, puntos)
        y_vals = [self.f_vel(t) for t in t_vals]
        plt.plot(t_vals, y_vals, label='v(t)', color='green')
        plt.title("Gráfica de velocidad")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Velocidad (m/s)")
        plt.grid(True)
        plt.legend()
        plt.show()

    def graficar_aceleracion(self, t_min, t_max, puntos=100):
        t_vals = np.linspace(t_min, t_max, puntos)
        y_vals = [self.f_acel(t) for t in t_vals]
        plt.plot(t_vals, y_vals, label='a(t)', color='red')
        plt.title("Gráfica de aceleración")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Aceleración (m/s²)")
        plt.grid(True)
        plt.legend()
        plt.show()


mov = Movimiento("3*t**2 - 4*t + 1")

# Mostrar ecuaciones
print(mov.mostrar_ecuaciones())

# Graficar de t = 0 a t = 5
mov.graficar_posicion(0, 5)
mov.graficar_velocidad(0, 5)
mov.graficar_aceleracion(0, 5)