import tkinter as tk

ventana =  tk.Tk()
ventana.geometry("500x400")

frame_superior = tk.Frame(ventana, bg="blue", width=300, height=100)
frame_superior.pack(side="top", fill=tk.X)

frame_inferior = tk.Frame(ventana, bg="red", width=300, height=100)
frame_inferior.pack(side="bottom", fill=tk.X)

frame_izquierdo = tk.Frame(ventana, bg="green", width=50)
frame_izquierdo.pack(side="left", fill=tk.BOTH)

frame_derecho = tk.Frame(ventana, bg="pink", width= 50)
frame_derecho.pack(side="right", fill=tk.BOTH, expand=True)

boton = tk.Button(frame_inferior, text="Salir", 
                  command="exit").pack(pady=2,side="right")

ventana.mainloop()