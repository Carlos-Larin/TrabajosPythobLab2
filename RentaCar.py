"""
Es el codigo para un concecionario de renta de carros encarrados
"""

class RentaCarElTillin():
    NombreCli=""
    Dui=""
    Nfon=""
    nombreVehiculo=""
    PrecioVehiculo=0
    DiasEnTenencia=0
    PrecioTotal=0

    def __init__(self):
        self.NombreCli=""
        self.Dui=""
        self.Nfon=""
        self.nombreVehiculo=""
        self.PrecioVehiculo=0
        self.DiasEnTenencia=0
        self.PrecioTotal=0

    def Calculo(self):
        self.PrecioTotal=(self.DiasEnTenencia*self.PrecioVehiculo)
        print(f"El Vehiculo que {self.NombreCli} lleva es el {self.nombreVehiculo} \n"
              f"El Precio total es de: ${round(self.PrecioTotal,4)}")
    
    def DatosClient(self):
        print(f"El nombre del cliente es: {self.NombreCli}\n"
              f"El numero de DUI: {self.Dui}\n"
              f"El numero de Telefono es: {self.Nfon}")
        
    def RegistraRenta(self):
        self.NombreCli=input("Nombre del cliente que renta: ")
        self.Dui=input("Ingrese el numero de Dui: ")
        self.Nfon=input("Ingrese el numero de Telefono: ")
        self.nombreVehiculo=input("Ingrese el nombre del vehiculo: ")
        self.PrecioVehiculo=float(input("Precio del vehiculo x dia: $"))
        self.DiasEnTenencia=int(input("La cantidad de Dias en tenencia: "))
    print("----------------------------------------------------------")
    def mostrarDatos(self):
        self.DatosClient()
        self.Calculo()
        print("----------------------------------------------------------")

Renta=RentaCarElTillin()
Renta.RegistraRenta()
print("----------------------------------------------------------")
Renta.mostrarDatos()
            