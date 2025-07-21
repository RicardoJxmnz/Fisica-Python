from calculadora_vector import*
from vector import*
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.pyplot as plt          
from tkinter import messagebox
          
class Dinamica:
    @staticmethod
    def calcularAceleracion(masa, cf, fuerzas, gravedad = 9.81):
        fuerza_x, fuerza_y = CalculadoraVector.suma_vector(fuerzas)
        fuerza_normal = - fuerza_y
        fuerza_friccion = cf * fuerza_normal
        print(fuerza_x)
        if fuerza_x > 0:
            return (fuerza_x - fuerza_friccion)/masa, VectorPolar(fuerza_normal, 90), VectorPolar(fuerza_friccion, 180)
        elif abs(fuerza_x) < 1e-8:
            return 0, VectorPolar(fuerza_normal, 90), VectorPolar(0, 0)
        else:
            return (-fuerza_x - fuerza_friccion)/masa, VectorPolar(fuerza_normal, 90), VectorPolar(fuerza_friccion, 0)
    
    
    @staticmethod
    def calcularCoeficiente(masa, aceleracion, fuerzas):
        fuerza_x, fuerza_y = CalculadoraVector.suma_vector(fuerzas)
        fuerza_normal = - fuerza_y
        return (fuerza_x - masa * aceleracion)/fuerza_normal



#####################################################################################################################################################################
class DinamicaInterfaz:
    """La lista colores permite ir graficando los vectores que agreguemos de un color diferente, NO SE AGREGA SELF
    YA QUE SE DETERMINA COMO VARIABLE ESTATICA, LO QUE SIGNIFICA QUE NO ES PROPIA DE LA INSTANCIA Y POR LO TANTO 
    TENDRA EL MISMO VALOR"""
    colores = ["red", "green", "blue", "yellow", "cyan", "magenta", "black", "white", "orange","purple",  
    "pink", "brown", "gray", "olive", "navy"]

#####################################################################################################################################################################
    """En el contructor de la interfaz se agregan todos los componentes de la misma, recuerde que el 
    termino self indica a las variables o metodos que son propios de la clase"""
    def __init__(self):
        # Crear ventana principal
        self.ventana = tk.Tk()             # Se crea la ventana 
        self.ventana.title("Dinamica")     # Agregamos un titulo a la ventana
        self.ventana.geometry("900x550")   # Determinamos el tamñao

        # Crear dos marcos: uno para los datos (izquierda), otro para la gráfica (derecha)
        self.frame_izquierdo = tk.Frame(self.ventana)
        self.frame_izquierdo.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.frame_derecho = tk.Frame(self.ventana)
        self.frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        #Creamos el combo box donde se permitira elegir que calculo se va a realiza
        self.opciones = ttk.Combobox(self.frame_izquierdo, values=["Calcular Aceleracion", "Calcular Coeficiente"]) #Se crea el combo con la lista de valores que necesitemos y se guarda en una variable
        self.opciones.pack() #Agrega el combo a la ventana organizándolo de forma automática según el espacio disponible
        self.opciones.bind("<<ComboboxSelected>>", self.calculo_seleccionado)  # Se vincula un evento para detectar cuando se selecciona una opción del combo

        # Campo de entrada para el componente x o magnitud (r)
        tk.Label(self.frame_izquierdo, text="Magnitud:").pack()  # Etiqueta descriptiva
        self.x_r = tk.Entry(self.frame_izquierdo)                # Campo de entrada
        self.x_r.pack()                                  # Se agrega a la ventana

        # Campo de entrada para el componente y o ángulo
        tk.Label(self.frame_izquierdo, text="Angulo:").pack()    # Etiqueta descriptiva
        self.y_angulo = tk.Entry(self.frame_izquierdo)           # Campo de entrada
        self.y_angulo.pack()                             # Se agrega a la ventana

        # Botón para crear un vector en forma polar
        tk.Button(self.frame_izquierdo, text="Agregar Vector", command=self.crear_polar).pack(pady=2)  # Al hacer clic, se ejecuta crear_polar

        # Lista para mostrar los vectores agregados
        self.lista_vectores = tk.Listbox(self.frame_izquierdo)   # Se crea un listbox para mostrar vectores
        self.lista_vectores.pack()                       # Se agrega a la ventana

        # Botón para eliminar un vector en especifico seleccionado en la listbox
        tk.Button(self.frame_izquierdo, text="Eliminar Vector", command=self.eliminar_vector).pack(pady=2)

        # Campo de entrada para la masa
        tk.Label(self.frame_izquierdo, text="Masa").pack()       # Etiqueta 
        self.masa = tk.Entry(self.frame_izquierdo)               # Campo de entrada para masa
        self.masa.pack()                                 # Se agrega a la ventana

        # Campo de entrada para el coeficiente de fricción
        tk.Label(self.frame_izquierdo, text="Coeficiente de friccion").pack()  # Etiqueta
        self.cf = tk.Entry(self.frame_izquierdo)                               # Campo de entrada
        self.cf.pack()                                                 # Se agrega a la ventana

        # Campo de entrada para mostrar o introducir la aceleración
        tk.Label(self.frame_izquierdo, text="Aceleracion").pack()  # Etiqueta
        self.aceleracion = tk.Entry(self.frame_izquierdo)          # Campo de entrada
        self.aceleracion.pack()                            # Se agrega a la ventana

        # Botón para calcular el resultado con base en los datos ingresados
        tk.Button(self.frame_izquierdo, text="Calcular", command=self.calcular).pack(pady=2)        # Ejecuta calcular
        tk.Button(self.frame_izquierdo, text="Eliminar datos", command=self.eliminar).pack(pady=2)  # Limpia los campos

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
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_derecho)        # Se vincula la figura a Tkinter
        self.canvas.get_tk_widget().pack(pady=10, fill=tk.BOTH, expand=True)  # Se empaqueta y permite expandirse

        # Lista para almacenar los vectores creados
        self.vectores = []  # Se inicializa como lista vacía

#####################################################################################################################################################################
    """La soguiente funcion permite crear los vectores y darle funcionalidad al boton de agregar vector
    creando un vector de forma polar ya que en los campos se agrega la magnitud y el angulo, y 
    se agrega a la lista de vectores ademas actualizar la grafica"""
    def crear_polar(self):
        """Creamos una excepcion, pero ¡que es lo que hace?: 
        EL contructor de vector requiere dos valores numericos, supongamos que el usuario por error ingresa una cadena de caracteres,
        un numero con los puntos mal situados, comas en lugar de puntos o simplemente deja algun campo vacio, esto podria generar 
        un error en cadena que bloquee nuestro programa, para evitar este problema usamos execepciones.
        Dentro del try se coloca todo aquello que se quiere poner a prueba en este caso la optencion de los datos
        y la creacion del vector, si esta prueba no genera ningun error procedera a agregar este vector a la lista y actualizar la grafica.
        Si el programa detecta algun error saltara esta seccion y ejecutara lo que se encuentra dentro del except, en este caso un mensaje 
        de error y asi evitara que existan problemas durante la ejecucion del programa"""
        try:
            # Crea el vector polar usando los valores ingresados por el usuario
            vector = VectorPolar(float(self.x_r.get()), float(self.y_angulo.get()))  # Convierte las entradas en flotantes y crea un objeto VectorPolar
            self.vectores.append(vector)           # Agrega el nuevo vector a la lista de vectores
            self.actualizar_grafica(self.vectores)              # Actualiza la lista visual y posiblemente el gráfico con los nuevos datos
        except:
            messagebox.showerror("Error", "Los datos ingresados son incorrectos.")  # Imprimimos un mensaje dado cualquier error detectado, como datos incopatibles, o campos vacios
        
#####################################################################################################################################################################
    """La siguiente funcion permite actualizar la grafica dependiendo de los vectores agregados a la lista y tambien permite
    mostrar estos en la listbox"""
    def actualizar_grafica(self, fuerzas):
        self.lista_vectores.delete(0, tk.END)  # Limpiar todo lo que se encuentre dentro de la listbox
        """Con este for agregamos cada uno de los vectores en la listbox imprimiendolo de la siguiente manera
        (r, angulo)--> f"({vector.r},{vector.angulo}°)"""
        for vector in self.vectores:
            """El tk.END permite agregar un valor nuevo en la ultima posicion por ejemplo, en la primera iteracion
            se imprimen los datos del primer vector hasta arriba de la lista, en la segunda interacion gragicas a tk.ENd
            nos permite agregar el nuevo vector por debajo del anterior, sin necesida de saber en que posicion o numero se quedo"""
            self.lista_vectores.insert(tk.END, f"({vector.r},{vector.angulo}°)")

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
            self.ax.set_xlim(min(*[v.x for v in fuerzas], 0) - 1, max(*[v.x for v in fuerzas], 0) + 1)  #Limite inferior y superior del eje x 
            #Para el eje y se realiza lo mismo que en el eje x
            self.ax.set_ylim(min(*[v.y for v in fuerzas], 0) - 1, max(*[v.y for v in fuerzas], 0) + 1)  #limite inferior y superior del eje y
            self.ax.grid(True)             # Activa el fondo cuadriculado
            self.ax.set_aspect('equal')    # Mantiene proporción 1:1 en la gráfica

            # Dibuja cada vector con su color y etiqueta
            for vector, color in zip(fuerzas, DinamicaInterfaz.colores):
                plt.quiver(0, 0, vector.x, vector.y, angles="xy", scale_units="xy",
                       scale=1, color=color, label=f"({vector.r:.2f}, {vector.angulo:.2f})")
            
            self.ax.legend()      # Muestra la leyenda con etiquetas de vectores
            self.canvas.draw()    # Refresca el lienzo en la interfaz
        except:
            """Si se detecto un error en try se genera la exepcion, como se habia comentado anteriormente, 
            el error se puede producir cuando no exista ningun vector dentro de la lista por ello se llama a la funcion de
            limpiar grafica simplemente"""
            self.limpiar_grafica()

#####################################################################################################################################################################
    """Enta funcion permite limpiar la grafica y restaurar los valores pedeterminados de la misma"""
    def limpiar_grafica(self):
        self.ax.clear()                            # Limpia la gráfica
        self.ax.axhline(0,color="black", lw=0.5)   # Redibuja el eje x
        self.ax.axvline(0,color="black", lw=0.5)   # Redibuja el eje y
        self.ax.set_xlim(-10, 10)                  # Restaura límites por defecto del eje x
        self.ax.set_ylim(-10, 10)                  # Restaura límites por defecto del eje y
        self.ax.grid(True)                         # Activa la cuadricula
        self.canvas.draw()                         # Refresca la gráfica
        self.vectores.clear()                      # Elimina todos los vectores"""

#####################################################################################################################################################################
    """Este metodo se ejecutara automaticamente cuando se detecte algun cambio dentro del combo box"""
    def calculo_seleccionado(self, event):
        """Cuando se ejecuta este metodo lo primero es prefuntarse que es lo que se selecciono dentro del combo
        si fue --Calcular Aceleracion--, bloqueamos el campo de aceleracion para que el usuario no pueda agregar 
        ningun valor, ya que esta debera ser calculada y asignada por el programa"""
        if self.opciones.get() == "Calcular Aceleracion":  # Si la opcion del combo es Calcular Aceleracion
            self.aceleracion.config(state="disabled")      # Bloqueamos el campo de aceleracion con "disabled"
            self.cf.config(state="normal")
        elif self.opciones.get() == "Calcular Coeficiente":
            self.cf.config(state="disabled")
            self.aceleracion.config(state="normal")

#####################################################################################################################################################################
    """Este metodo llama al metodo de calcular aceleracion de la clase Dinamica y le de funcionalidad al boton de calcular"""
    def calcular(self):
        fuerzas = []
        if self.opciones.get() == "Calcular Aceleracion":   # Si la opcion del combo es Calcular Aceleracion
            self.aceleracion.config(state="normal")         # Desbloqueamos el campo de aceleracion con "normal" para poder modificarlo
            self.aceleracion.delete(0, tk.END)              # Limpiamos el campo con delete
            """Con esta exepcion determinamos si los valores de la masa y el coeficiente de friccion son validos
            si no mandara un error """
            try:
                # Insertamos el valor que retornara la funcion de calcular aceleracion con insert, debemos de colocar el 0 antes de lo que vayamos a colocar en el campo
                # Con str convertimos el valor flotante que devuelve la funcion en una cadena de caracteres para que sea compatible con la funcion de insert
                # LLamamos al metodo de calcular aceleracion con los argumentos de masa y coeficiente obtenidos de cuadros de texto
                # el float es para convertir la cadena de caracteres leida a un valor flotante
                aceleracion, fuerza_normal, fuerza_friccion =  Dinamica.calcularAceleracion(float(self.masa.get()), 
                                             float(self.cf.get()), self.vectores)
                self.aceleracion.insert(0, str(aceleracion))  
                fuerzas = self.vectores.copy()
                fuerzas.append(fuerza_normal)
                fuerzas.append(fuerza_friccion)
                self.actualizar_grafica(fuerzas)
            except Exception as e:
                 print(e)
                 messagebox.showerror("Error", "Los datos ingresados son incorrectos.")  # Imprimimos un mensaje dado cualquier error detectado, como datos incopatibles, o campos vacios
            """Una vez modificado el campo volvemos a bloquearlo"""
            self.aceleracion.config(state="disabled")   # Bloqueamos el campo de aceleracion con "disabled"
        elif self.opciones.get() == "Calcular Coeficiente":
            self.cf.config(state="normal")         # Desbloqueamos el campo de aceleracion con "normal" para poder modificarlo
            self.cf.delete(0, tk.END)              # Limpiamos el campo con delete
            """Con esta exepcion determinamos si los valores de la masa y el coeficiente de friccion son validos
            si no mandara un error """
            try:
                # Insertamos el valor que retornara la funcion de calcular aceleracion con insert, debemos de colocar el 0 antes de lo que vayamos a colocar en el campo
                # Con str convertimos el valor flotante que devuelve la funcion en una cadena de caracteres para que sea compatible con la funcion de insert
                # LLamamos al metodo de calcular aceleracion con los argumentos de masa y coeficiente obtenidos de cuadros de texto
                # el float es para convertir la cadena de caracteres leida a un valor flotante
                self.cf.insert(0, str(
                    Dinamica.calcularCoeficiente(float(self.masa.get()), 
                                             float(self.aceleracion.get()), self.vectores))[1])  
            except:
                 messagebox.showerror("Error", "Los datos ingresados son incorrectos.")  # Imprimimos un mensaje dado cualquier error detectado, como datos incopatibles, o campos vacios
            """Una vez modificado el campo volvemos a bloquearlo"""
            self.cf.config(state="disabled")   # Bloqueamos el campo de aceleracion con "disabled"

#####################################################################################################################################################################
    """Este metodo permite eliminar todos los datos y campos que existan en la interfaz"""
    def eliminar(self):
        self.limpiar_grafica()                 # LLamamos al metodo de limpiar grafica
        self.x_r.delete(0, tk.END)             # Borramos lo que se encuentre en el campo de magnitud
        self.y_angulo.delete(0, tk.END)        # Limpiamos el campo de angulo
        self.cf.delete(0, tk.END)              # Limpiamos el campo de coeficiente de friccioon
        self.aceleracion.delete(0, tk.END)     # Limpiamos el campo de aceleracion
        self.masa.delete(0, tk.END)            # Limpiamos el campo de masa
        self.lista_vectores.delete(0, tk.END)  # Limpiamos la listbox 

#####################################################################################################################################################################
    """Este metodo permite eliminar un vector seleccionado en la listbox"""
    def eliminar_vector(self):
        # Con self.lista_vectores.curselection()[0] determinamos la posicion en la cual se encuentra el vector a eliminar
        # Con pop eliminamos el vector de la lista principal
        self.vectores.pop(self.lista_vectores.curselection()[0])

        # Una vez eliminado el vector seleccionado actualizamos la grafica
        self.actualizar_grafica(self.vectores)

#####################################################################################################################################################################
    """Este metodo permite mostra la interfaz, si no se llama aunque instanciemos la clase no se mostrara nada"""
    def mostrar(self):
        self.ventana.mainloop()   # Muestra la ventana configurada en pantalla

#####################################################################################################################################################################

# Instanciamos la clase de Dinamica Interfaz
interfaz = DinamicaInterfaz()
# Mostramos la interfaz
interfaz.mostrar()


