
#este codigo es de manera simple

mensaje = "Hola Carva"
print(mensaje)


num1 = int(input("Porfavor ingresa el num 1: "))

num2 = int(input("Porfavor ingresa el num 2: "))

print("Ingresa un numero segun la obcion que quiereas obtener\n 1: Suma\n 2: Resta\n 3: Multiplicacion \n 4: Division\n")
opcion = int(input("Obcion a elegir: "))

if opcion == 1:
    result = num1 + num2
    print(f"La respuesta de la {opcion}:suma de {num1} y {num2} es: {result}")     
elif opcion ==2:
    result = num1 - num2
    print(f"La respuesta de la {opcion}:Resta de {num1} y {num2} es: {result}") 
elif opcion ==3:
    result = num1 * num2
    print(f"La respuesta de la {opcion} de num1 y num2 es: {result}") 
elif opcion ==4:
    if num2 !=0:
        result = num1 // num2
        print(f"La respuesta de la {opcion} de {num1} y {num2} es: {result}") 
    else:  
        print("No se puede dividir por cero.")
else:
    print("obcion equivocada")
    


#este codigo es para web
"""
import streamlit as st

# Mostrar un mensaje en la aplicación web
st.write("Hola Carva")

# Solicitar entrada del usuario
num1 = st.number_input("Por favor, ingresa el num 1:", value=0, step=1)
num2 = st.number_input("Por favor, ingresa el num 2:", value=0, step=1)

# Mostrar las opciones al usuario
opcion = st.selectbox("Ingresa un número según la opción que quieras obtener",
                      ("Seleccionar", "Suma", "Resta", "Multiplicación", "División"))

# Botón para realizar la operación
if st.button("Calcular"):
    if opcion == "Seleccionar":
        st.write("Por favor, selecciona una opción válida.")
    elif opcion == "Suma":
        result = num1 + num2
        st.write(f"La respuesta de la suma de {num1} y {num2} es: {result}")
    elif opcion == "Resta":
        result = num1 - num2
        st.write(f"La respuesta de la resta de {num1} y {num2} es: {result}")
    elif opcion == "Multiplicación":
        result = num1 * num2
        st.write(f"La respuesta de la multiplicación de {num1} y {num2} es: {result}")
    elif opcion == "División":
        if num2 != 0:
            result = num1 / num2
            st.write(f"La respuesta de la división de {num1} y {num2} es: {result}")
        else:
            st.write("No se puede dividir por cero.")
"""
"""
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
"""