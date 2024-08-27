class donas():
    tipo=""
    cantidad=0
    precio=0
    Ptotal=0
    Sabor=""
    def __init__(self):
        self.tipo=""
        self.cantidad=0
        self.precio=0
        self.Ptotal=0
        self.Sabor=""

    def TomarOrden(self):
        #g=grande
        if(self.tipo=="g" or self.tipo=="grande"):
            self.precio=(self.cantidad*0.25)
            print(f"El tipo de dona es Grande y llevas la cantidad de: {self.cantidad} ")
        #p=pequeño    
        elif(self.tipo=="p" or self.tipo=="pequeña"):
            self.precio=(self.cantidad*0.15)
            print(f"El tipo de dona es Pequeño y llevas la cantidad de: {self.cantidad} ")
        else:
            print("No tenemos de esa obcion :(")
    
    def registro(self):
        self.tipo=input("Elija el tamaño de las donas: (G=Grande/P=Pequeña) ").lower()
        self.cantidad=int(input("Elija la cantidad de unidades que llevara: "))
        self.Sabor=input("De que sabor la quiere: ")
        
    def mostrarDatos(self):
        print("Gracias por preferirnos")
        self.TomarOrden()
        print(f"Sabor de la dona: {self.Sabor}")
        print(f"Precio a pagar: {self.precio}")
"""
    print("_____")
        print(f"Total a pagar: {round(self.PrecioVenta + self.Preciosoda, 2)}")
        print(f"Pago recibido: {self.mepagan}")
        print(f"Cambio: {self.Cambio}")
"""

orden=donas()
print("*****************************************")
orden.registro()
print("*****************************************")
orden.mostrarDatos()
print("*****************************************")

