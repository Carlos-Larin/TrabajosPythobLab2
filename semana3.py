#listas
        #0          1       2       3
lista1=["Carlos","Maria","Pedro","Juan"]
        #-4         -3     -2      -1 
print(lista1[0])
print(lista1[-1])

lista2=[4,6,"Agua",True,4.5]
print(lista2)

print(lista2.index("Agua"))


lista3=["Ingles","Matematicas","Lenguaje"]
lista3.append("Ciencias")
print(lista3)

lista3.insert(3,"Sociales")
print(lista3)

lista3[1]="Matematica"
print(lista3)

lista3.remove("Lenguaje")
print(lista3)
#indices
lista3.pop(0)
print(lista3)

#ordenar
lista3.sort(reverse=True)
print(lista3)

#longitud
print(len(lista3))

#las tuplas son intocables ya una vez creadas
tupla1=("San Miguel","La Union","Usulutan","Morazan")
print(tupla1[1])
#tupla1[1]="San Vicente"

#conjuntos
conjunto1={4,8,9,10,15,15}
print(conjunto1)
#conjunto[0]=1
conjunto1.add(7)
print(conjunto1)
conjunto1.remove(10)
print(conjunto1)

#diccionarios
di={"persona1":"Maria","persona2":"Juana","persona3":"Perez"}
print(di)
print(di["persona1"])


#act. clase

Agentes=["Viper","Fade","Skye","DeadLock"]
print(Agentes[1])
print(Agentes[-2])

Agentes=["Viper","Fade","Skye","DeadLock"]
tuplaMapas=("Abyss","Lotus","Mind")
print(f"En el mapa de {tuplaMapas[2]} es mejor llevar a {Agentes[-2]}")

print(Agentes.key())