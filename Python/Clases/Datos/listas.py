lista =["A","B","C"]
lista2 = [1, 65, 0]
lista3 = ["A", 54, True, False]

lista4 = list("Python")

print(lista4)

l1  = [1,2,3,4]
l2 = list(l1)#crear y copiar listas
l2.append(5)
print(l1)

#acceso a elementos
print(lista4[2])

#sublista - aplica lo mismo que sub cadenas

#funciones que no modifican las listas
print(len(lista))#Tamaño de la lista 
print(max(lista2))#Toma el valos maximo de un lista
print(54 in lista3)
print(lista3.count(54))#cuantas veces hay un elemento en la lista 
print(all(lista3))#si todos los datos son verdaderos
print(any(lista3))#Si algun dato es verdadero
print("**********************")
print(lista.index("B"))#entrega el valor de la posicion

#operaciones que si afectan a las listas
print(lista + lista2)#nueva lista con los elementos de ambas 
lista.append("D")#agregamos elemento al final
print(lista)
lista.pop()
print(lista)#eliminamos el ultimo elemento
lista.insert(1, "H")#inserto un elemento en una posicion deseada
print(lista)
lista3.remove(54)
print(lista3)

