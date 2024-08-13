
#lower() upper()
"""
usuario=input("Hola ¿como te llamas?: ")
print(f"!Hola {usuario.upper()}¡")
"""

#un saludo con str. y \n para un salto de linea y el *10 la veces que se repite
"""
nombre= "Aristides"
apellido="Larin"

print(f"Hola mundo yo soy {nombre} y mi apellido es {apellido}\n"*10)
"""

#funciones
def doblar_valor(numero):
    n2= numero*2
    return n2
print(doblar_valor(6))

def describir(tipom,nombrem):
    print(f"Mi mascota es un {tipom} y se llama {nombrem}")

describir("gato","juan")
describir("pejelagarto","lucas")
describir("chucho","pablo")
describir(nombrem="marta",tipom="pez")

int("Hola"," yo soy ","un hombre ", "muy guapo")