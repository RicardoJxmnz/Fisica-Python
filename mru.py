import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MRU:
    @staticmethod
    def calcular_posicion(posicion_inicial, velocidad, tiempo):
        return posicion_inicial + velocidad * tiempo
    
    @staticmethod
    def calcula_posicion_inicial(posicion, velocidad, tiempo):
        return posicion - velocidad * tiempo

    @staticmethod
    def calcular_velocidad(posicion_inicial, posicion, tiempo):
        return (posicion - posicion_inicial)/tiempo
    
    @staticmethod
    def calcular_tiempo(posicion_inicial, posicion, velocidad):
        return (posicion - posicion_inicial) / velocidad
    

class MruInterfaz:
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
            self.ventana.title("MRU")     # Agregamos un titulo a la ventana
            self.ventana.geometry("300x200")   # Determinamos el tamñao


        frame_superior = tk.Frame(self.ventana, width=300, height=100)
        frame_superior.pack(side="top", fill=tk.X)

        frame_inferior = tk.Frame(self.ventana, width=300, height=100)
        frame_inferior.pack(side="bottom", fill=tk.X)

        frame_izquierdo = tk.Frame(self.ventana, width=50)
        frame_izquierdo.pack(side="left", fill=tk.BOTH , expand=True)

        frame_derecho = tk.Frame(self.ventana, width= 50)
        frame_derecho.pack(side="right", fill=tk.BOTH, expand=True)

        tk.Label(frame_superior, text="MRU", font=("Arial", 20)).pack()

        #Creamos el combo box donde se permitira elegir que calculo se va a realiza
        self.opciones = ttk.Combobox(frame_superior, values=["Calcular Posicion", 
            "Calcular Posicion Inicial", "Calcular Velocidad", "Calcular Tiempo"]) #Se crea el combo con la lista de valores que necesitemos y se guarda en una variable
        self.opciones.pack() #Agrega el combo a la ventana organizándolo de forma automática según el espacio disponible
        self.opciones.bind("<<ComboboxSelected>>", self.calculo_seleccionado)  # Se vincula un evento para detectar cuando se selecciona una opción del combo

        tk.Label(frame_izquierdo, text="Posicion Inicial:").pack()  # Etiqueta de X0
        self.x0 = tk.Entry(frame_izquierdo)                # Campo de entrada
        self.x0.pack()

        tk.Label(frame_derecho, text="Posicion Final:").pack()  # Etiqueta descriptiva
        self.x = tk.Entry(frame_derecho)                # Campo de entrada
        self.x.pack()

        tk.Label(frame_izquierdo, text="Velocidad:").pack()  # Etiqueta descriptiva
        self.v = tk.Entry(frame_izquierdo)                # Campo de entrada
        self.v.pack()

        tk.Label(frame_derecho, text="Tiempo:").pack()  # Etiqueta descriptiva
        self.t = tk.Entry(frame_derecho)                # Campo de entrada
        self.t.pack()

        # Botón para calcular el resultado con base en los datos ingresados
        tk.Button(frame_inferior, text="Calcular", 
                  command=self.calcular).pack(pady=2)
    

    def calculo_seleccionado(self, event):
        opcion = self.opciones.get()

        if opcion == "Calcular Posicion":
            self.x.config(state="disabled")
            self.x0.config(state="normal")
            self.v.config(state="normal")
            self.t.config(state="normal")

        elif opcion == "Calcular Posicion Inicial":
            self.x0.config(state="disabled")
            self.x.config(state="normal")
            self.v.config(state="normal")
            self.t.config(state="normal")

        elif opcion == "Calcular Velocidad":
            self.v.config(state="disabled")
            self.x0.config(state="normal")
            self.x.config(state="normal")
            self.t.config(state="normal")

        elif opcion == "Calcular Tiempo":
            self.t.config(state="disabled")
            self.x0.config(state="normal")
            self.x.config(state="normal")
            self.v.config(state="normal")

    def calcular(self):
        try:
            if self.opciones.get() == "Calcular Posicion":
                self.x.config(state="normal") 
                resultado = MRU.calcular_posicion(float(self.x0.get()), float(self.v.get()), float(self.t.get()))
                self.x.config(state="normal")
                self.x.delete(0, tk.END)
                self.x.insert(0, str(resultado))
                self.x.config(state="disabled")

            elif self.opciones.get() == "Calcular Posicion Inicial":
                self.x0.config(state="normal")
                resultado = MRU.calcula_posicion_inicial(float(self.x.get()), float(self.v.get()), float(self.t.get()))
                self.x0.config(state="normal")
                self.x0.delete(0, tk.END)
                self.x0.insert(0, str(resultado))
                self.x0.config(state="disabled")

            elif self.opciones.get() == "Calcular Velocidad":
                self.v.config(state="normal")
                resultado = MRU.calcular_velocidad(float(self.x0.get()), float(self.x.get()), float(self.t.get()))
                self.v.config(state="normal")
                self.v.delete(0, tk.END)
                self.v.insert(0, str(resultado))
                self.v.config(state="disabled")

            elif self.opciones.get() == "Calcular Tiempo":
                self.t.config(state="normal")
                resultado = MRU.calcular_tiempo(float(self.x0.get()), float(self.x.get()), float(self.v.get()))
                self.t.config(state="normal")
                self.t.delete(0, tk.END)
                self.t.insert(0, str(resultado))
                self.t.config(state="disabled")
        except ValueError:
            messagebox.showerror("Error", "Los datos ingresados son incorrectos.")

    def mostrar (self):
        self.ventana.mainloop()
