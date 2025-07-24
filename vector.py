import math
from tkinter import messagebox

class Vector:
    def __init__(self,x, y, r, angulo):
        self.x = x
        self.y = y
        self.r = r
        self.angulo = angulo

class VectorPolar(Vector):
    def __init__(self, r, angulo):
        x = r * math.cos(math.radians(angulo))
        y = r * math.sin(math.radians(angulo))
        super().__init__(x, y, r, angulo)
        
    def set_r(self, r):
        self.r = r
        self.x = r * math.cos(math.radians(self.angulo))
        self.y = r * math.sin(math.radians(self.angulo))
        
    def set_angulo(self, angulo):
        self.angulo = angulo
        self.x = self.r * math.cos(math.radians(angulo))
        self.y = self.r * math.sin(math.radians(angulo))

class VectorRectangular(Vector):
    def __init__(self, x, y):
        r = math.sqrt(x**2 + y**2)
        angulo = self.calcular_angulo(x, y)
        super().__init__(x, y, r, angulo)

    @staticmethod
    def calcular_angulo(x, y):
        angulo = math.degrees(math.atan(y/x))
        if x >= 0 and y >= 0:
            return angulo
        elif (x<0 and y>=0) or (x<0 and y<0):
            return 180 + angulo
        else:
            return 360 + angulo
    
    def set_x(self, x):
        self.x = x
        self.r = math.sqrt(x**2 + self.y**2)
        self.angulo = self.calcular_angulo(x, self.y)

    def set_y(self, y):
        self.y = y
        self.r = math.sqrt(self.x**2 + y**2)
        self.angulo = self.calcular_angulo(self.x, y)
    
class InstanciaVector:
    @staticmethod
    def crear_polar(self, r, angulo):
        try:
            vector = VectorPolar(r, angulo)  # Convierte las entradas en flotantes y crea un objeto VectorPolar
        except:
            messagebox.showerror("Error", "Los datos ingresados son incorrectos.")
        return vector
