#ventana flotante
from tkinter import *
from tkinter import ttk

ventana = Tk()
#tamanio
ventana.geometry("500x500") 
#color
ventana.config(bg="#EBDEF0")
#titulo
ventana.title("Hola primera pagina en ventana")

frml = ttk.Frame(ventana,padding=10)
frml.grid()
ttk.Label(frml, text="Hola mundo este es el primer bloque del codigo")
ttk.Button(frml, text="Adios", command=ventana.destroy).grid(column=1,row=0)

frml = ttk.Frame(ventana,padding=10)
frml.grid()
ttk.Label(frml, text="Hola Dekbre").grid(column=0,row=0)
ttk.Button(frml, text="Cerrar", command=ventana.destroy ).grid(column=1, row=0)

ventana.mainloop