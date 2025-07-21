from sympy import symbols, Eq, solve

x = symbols('x')  # Definimos la variable simbólica x
ecuacion = Eq(x**2 - 4, 0)  # Creamos la ecuación x² - 4 = 0
soluciones = solve(ecuacion, x)  # Resolvemos la ecuación
print(soluciones)  # Mostramos las soluciones: [2, -2]



x = symbols('x')  # Definimos la variable x
expresion = x**2 + 2*x + 1  # Definimos la expresión algebraica
valor = expresion.subs(x, 3)  # Sustituimos x por 3 en la expresión
print(valor)  # Mostramos el resultado: 16



x, y = symbols('x y')  # Definimos dos variables simbólicas: x y y
ec1 = Eq(2*x + y, 10)  # Primera ecuación: 2x + y = 10
ec2 = Eq(x - y, 2)     # Segunda ecuación: x - y = 2

sol = solve((ec1, ec2), (x, y))  # Resolvemos el sistema de ecuaciones
print(sol)  # Mostramos la solución: {x: 4, y: 2}



import numpy as np  # Importamos numpy para manejo de arrays numéricos
import matplotlib.pyplot as plt  # Importamos matplotlib para graficar
x = np.linspace(-10, 10, 400)  # Creamos un arreglo de 400 valores entre -10 y 10
y = x**2 - 4  # Calculamos y para cada x (función y = x² - 4)

plt.plot(x, y)  # Dibujamos la gráfica de la función
plt.axhline(0, color='gray', linestyle='--')  # Línea horizontal para indicar y = 0
plt.title("Gráfica de y = x² - 4")  # Título de la gráfica
plt.grid(True)  # Activamos la cuadrícula
plt.show()  # Mostramos la gráfica