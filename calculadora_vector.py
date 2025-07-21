from vector import*
import matplotlib.pyplot as plt 

class CalculadoraVector:
    @staticmethod
    def suma_vector(vectores):
        x = 0
        y = 0
        for vector in vectores:
            x = x + vector.x
            y = y + vector.y
        return x, y
    
    def resta_vector(self, vector1, vector2):
        pass

    def multiplicacion_vector(self, vector1, vector2):
        pass

    def division_vector(self, vector1, vector2):
        pass

    def graficar_vector(self, vector):
        plt.figure()

        plt.axhline(0,color="black", lw=0.5)
        plt.axvline(0,color="black", lw=0.5)

        plt.quiver(0, 0, vector.x, vector.y, angles="xy", scale_units="xy", 
                   scale=1, color="r", label=f"({vector.x},{vector.y})")
        
        plt.xlim(min(0,vector.x)-1, max(0,vector.x)+1)
        plt.ylim(min(0,vector.y)-1, max(0,vector.y)+1)

        plt.grid(True)
        plt.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Grafica Vector")

        plt.show()


    
"""vec1 = VectorRectangular(3,4)
vec2 = VectorPolar(4,30)

calculadora = CalculadoraVector()
print(calculadora.suma_vector(vec1, vec2))
calculadora.graficar_vector(vec1)"""