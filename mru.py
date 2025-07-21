import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MRU:
    @staticmethod
    def calcular_posiciom(posicion_inicial, velocidad, tiempo):
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
    def __init__(self):
        # Crear ventana principal
        self.ventana = tk.Tk()             # Se crea la ventana 
        self.ventana.title("MRU")     # Agregamos un titulo a la ventana
        self.ventana.geometry("400x300")   # Determinamos el tamñao

        tk.Label(self.ventana, text="MRU", font=("Arial", 20)).pack()

        #Creamos el combo box donde se permitira elegir que calculo se va a realiza
        self.opciones = ttk.Combobox(self.ventana, values=["Calcular Posicion", 
            "Calcular Posicion Inicial", "Calcular Velocidad", "Calcular Tiempo"]) #Se crea el combo con la lista de valores que necesitemos y se guarda en una variable
        self.opciones.pack() #Agrega el combo a la ventana organizándolo de forma automática según el espacio disponible
        self.opciones.bind("<<ComboboxSelected>>", self.calculo_seleccionado)  # Se vincula un evento para detectar cuando se selecciona una opción del combo

        tk.Label(self.ventana, text="Posicion Inicial:").pack()  # Etiqueta de X0
        self.x0 = tk.Entry(self.ventana)                # Campo de entrada
        self.x0.pack()

        tk.Label(self.ventana, text="Posicion Final:").pack()  # Etiqueta descriptiva
        self.x = tk.Entry(self.ventana)                # Campo de entrada
        self.x.pack()

        tk.Label(self.ventana, text="Velocidad:").pack()  # Etiqueta descriptiva
        self.v = tk.Entry(self.ventana)                # Campo de entrada
        self.v.pack()

        tk.Label(self.ventana, text="Tiempo:").pack()  # Etiqueta descriptiva
        self.t = tk.Entry(self.ventana)                # Campo de entrada
        self.t.pack()

        # Botón para calcular el resultado con base en los datos ingresados
        tk.Button(self.ventana, text="Calcular", command=self.calcular).pack(pady=2)
    

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

