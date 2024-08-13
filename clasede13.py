""""""
class libro():
    def __init__(self,tit,auto,edic):
        self.titulo=tit
        self.autor=auto
        self.edicion=edic
        self.editorial="El tilin del Salvador"
        #aqui es donde meteremos los datos
    
    def datos(self):
        print(f"Titulo: {self.titulo} Autor: {self.autor}")

#aqui es donde rellenamos los datos
libro1 = libro("Un cartero","Charles","Primera edicion")
libro1.datos()