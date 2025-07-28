import tkinter as tk
from dinamica import DinamicaInterfaz
from mru import MruInterfaz

#Funcion que se ejecuta al precionar el boton
def abrir_mru():
    #Con este for limipiamos todos los widjets del frame
    for widjet in frame_derecho.winfo_children():
        widjet.destroy()
    # De esta forma creamos la interfaz de MRU dentro del frame especificado dentro del parentesis
    mru = MruInterfaz(frame = frame_derecho)

#Funcion que se ejecuta la interfaz de Dinamica
def abrir_dinamica():
    for widjet in frame_derecho.winfo_children():
        widjet.destroy()
    dinamica = DinamicaInterfaz(frame = frame_derecho)

# Crear ventana principal
ventana = tk.Tk()             # Se crea la ventana 
ventana.title("Dinamica")     # Agregamos un titulo a la ventana
ventana.geometry("900x550")   # Determinamos el tamñao

# Frame para colocar el boton
frame_izquierdo = tk.Frame(ventana, width=150)
frame_izquierdo.pack(side="left", fill=tk.BOTH)
frame_izquierdo.pack_propagate(False) # Con esta funcion evita que el frame se contraiga por la medida del boton

# Frame donde se abrira la interfaz
frame_derecho = tk.Frame(ventana, width= 50)
frame_derecho.pack(side="right", fill=tk.BOTH, expand=True)

#Boton que abrira el la interfaz de MRU
tk.Button(frame_izquierdo, text="MRU", command=abrir_mru).pack(pady=10)
# Boton para abrir Dinamica
tk.Button(frame_izquierdo, text="Dinamica", command=abrir_dinamica).pack(pady=10)  

ventana.mainloop()