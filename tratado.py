import tkinter as tk
from tkinter import messagebox, filedialog

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Hola vent")
ventana.geometry("500x300")

class ElPerroj():
    def __init__(self):
        self.Tipo = "Perro"
        self.NombrePerro = ""
        self.Raza = ""
        self.Edad = 0
        self.ColorPelaje = ""
        self.Dueño = ""
        self.Peso = 0
        self.Estado = "No Atendido"

    def DatosPerro(self, Tipo, NomPer, RazaBand, Edad, ColorPelaje, Dueño, PesoPerro, Estado):
        self.Tipo = Tipo
        self.NombrePerro = NomPer
        self.Raza = RazaBand
        self.Edad = Edad
        self.ColorPelaje = ColorPelaje
        self.Dueño = Dueño
        self.Peso = PesoPerro
        self.Estado = Estado

    def MostrarDatosPerro(self):
        datos = f"""**************Doctor Chopper****************
        Nombre: {self.NombrePerro}
        Raza: {self.Raza}
        Edad: {self.Edad} años
        Color del Pelaje: {self.ColorPelaje}
        Dueño: {self.Dueño}
        Peso: {self.Peso} kg
        Estado: {'Atendido' if self.Estado == 's' else 'No Atendido'}
        *****************************************"""
        messagebox.showinfo("Datos del Perro", datos)

# Función para manejar el evento del botón
def registrar_perro():
    NomPer = entry_nombre.get()
    RazaBand = entry_raza.get()
    Edad = int(entry_edad.get())
    ColorPelaje = entry_color.get()
    Dueño = entry_dueno.get()
    PesoPerro = int(entry_peso.get())
    Estado = entry_estado.get().lower()

    perro1.DatosPerro("Perro", NomPer, RazaBand, Edad, ColorPelaje, Dueño, PesoPerro, Estado)
    perro1.MostrarDatosPerro()

# Creación de una instancia de ElPerroj
perro1 = ElPerroj()

# Creación de widgets en la ventana donde ingresar datos
tk.Label(ventana, text="Nombre de la Mascota:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Raza:").pack()
entry_raza = tk.Entry(ventana)
entry_raza.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Color del Pelaje:").pack()
entry_color = tk.Entry(ventana)
entry_color.pack()

tk.Label(ventana, text="Dueño:").pack()
entry_dueno = tk.Entry(ventana)
entry_dueno.pack()

tk.Label(ventana, text="Peso (kg):").pack()
entry_peso = tk.Entry(ventana)
entry_peso.pack()

tk.Label(ventana, text="¿El perro fue atendido? (s/n):").pack()
entry_estado = tk.Entry(ventana)
entry_estado.pack()

# Botón para registrar los datos
tk.Button(ventana, text="Registrar Perro", command=registrar_perro).pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
