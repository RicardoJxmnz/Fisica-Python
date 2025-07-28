import tkinter as tk
from mru import MruInterfaz
from dinamica import DinamicaInterfaz

#Funcion que se ejecuta al selecciona MRU con el menu
def abrir_mru():
    #Con este for limipiamos todos los widjets del frame
    for widjet in frame_contenido.winfo_children():
        widjet.destroy()
    # De esta forma creamos la interfaz de MRU dentro del frame indicado
    mru = MruInterfaz(frame = frame_contenido)

#Funcion que se ejecuta la interfaz de Dinamica
def abrir_dinamica():
    for widjet in frame_contenido.winfo_children():
        widjet.destroy()
    dinamica = DinamicaInterfaz(frame = frame_contenido)

# Crear ventana principal
ventana = tk.Tk()             # Se crea la ventana 
ventana.title("Dinamica")     # Agregamos un titulo a la ventana
ventana.geometry("900x550")   # Determinamos el tamaño

# Frame principal donde se cargaran las sitintas interfaces
frame_contenido = tk.Frame(ventana)
frame_contenido.pack(fill=tk.BOTH, expand=True)

# Crear la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu = barra_menu)  # Asignar la barra a la ventana

# Crear el menú "Opciones"
menu_opciones = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Opciones", menu = menu_opciones)

# Agregar opciones al menú "Archivo"
menu_opciones.add_command(label="MRU", command=abrir_mru)
menu_opciones.add_separator()  # Línea separadora
menu_opciones.add_command(label="Dinámica", command=abrir_dinamica)

# Si quisieran crear otro menu 
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=lambda: print("Hecho con Tkinter"))

ventana.mainloop()
