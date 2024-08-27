class donas():
    tipo=""
    cantidad=0
    precio=0
    preciototal=0
    sabor=""
    glaseado=""
    topping=""

    def __init__(self):
        self.tipo= ""
        self.cantidad=0
        self.precio=0
        self.preciototal=0
        self.sabor=""
        self.glaseado=""
        self.topping=""
 
    def tomarorden(self):
        if(self.tipo == "g" or self.tipo=="grande"):
            self.precio=(self.cantidad * 0.25)
            print(f"El tamano de la dona es grande y llevas la cantidad de {self.cantidad}")
        elif(self.tipo=="p" or self.tipo=="pequeña"):
            self.precio=(self.cantidad * 0.15)
            print(f"El tamano de la dona es pequena y llevas la cantidad de {self.cantidad}")
        else:
            print("No lo escribiste bien, intenta escribiendo todo con minusculas")
   
    def registro(self):
        self.tipo=input("Elija el tamaño de las donas (g=grande/p=pequeña) > ").lower()
        self.cantidad=int(input("Elija la cantidad de unidades que llevara > "))
        self.sabor= input("Elija el sabor de la masa > ")
        self.glaseado= input("Elija el color del glaseado > ")
        self.topping= input("Elija el topping > ")
 
    def mostrardato(self):
        print("GRACIA POR COMPRARME")
        self.tomarorden()
        print(f"El color del glasseado es: {self.glaseado}")
        print(f"El topping es de: {self.topping}")
        print(f"Precio a pagar: {self.precio}")
        
 
orden=donas()
print("//////////////////////////////////////")
orden.registro()
print("//////////////////////////////////////")
orden.mostrardato()
print("//////////////////////////////////////")
