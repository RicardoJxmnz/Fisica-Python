import tkinter as tk
from mru import MruInterfaz
from dinamica import DinamicaInterfaz

#Funcion que se ejecuta al precionar el boton
def abrir_mru():
    # De esta forma creamos y abrimos una ventana secundaria, notese que dentro de los parentesis
    # se agrega la ventana principal de este codigo
    mru = MruInterfaz(ventana_principal=ventana)

    # Bloquear la ventana principal, para ello nos referimos a la ventana del obejto mru,
    # es por ello que se coloca ventana despues de mru.
    mru.ventana.grab_set()

    #Pausamos el codigo de la ventana principal, mientras la ventana secundaria se encuentre en ejecucion
    ventana.wait_window(mru.ventana)

#Funcion que se ejecuta la interfaz de Dinamica
def abrir_dinamica():
    dinamica = DinamicaInterfaz()
    dinamica.ventana.grab_set()
    ventana.wait_window(dinamica.ventana)

# Crear ventana principal
ventana = tk.Tk()             # Se crea la ventana 
ventana.title("Dinamica")     # Agregamos un titulo a la ventana
ventana.geometry("200x200")   # Determinamos el tamaño

# Boton para abrir MRU
tk.Button(ventana, text="MRU", command=abrir_mru).pack(pady=10) 
# Boton para abrir Dinamica
tk.Button(ventana, text="Dinamica", command=abrir_dinamica).pack(pady=10) 

ventana.mainloop()