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
libro1 = libro("No me mires los pechos","Charles","Cuarta edicion")
libro1.datos()