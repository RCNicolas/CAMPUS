# Lista anidada usando corchetes
#______________________________________________________________________________________________________________________________________
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Lista anidada usando la función list()
#______________________________________________________________________________________________________________________________________
lista_anidada = list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#Acceso a elementos de listas anidadas
#______________________________________________________________________________________________________________________________________
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(lista_anidada[0])      # Salida: [1, 2, 3]
print(lista_anidada[1])      # Salida: [4, 5, 6]
print(lista_anidada[0][1])   # Salida: 2
print(lista_anidada[2][0])   # Salida: 7

#Modificación de elementos en listas anidadas
#______________________________________________________________________________________________________________________________________
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_anidada[0][1] = 10
print(lista_anidada[0])      # Salida: [1, 10, 3]
lista_anidada[2][2] = 0
print(lista_anidada[2])      # Salida: [7, 8, 0]

#Longitud de listas anidadas
#______________________________________________________________________________________________________________________________________
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
longitud_total = 0
for sublista in lista_anidada:
    longitud_total += len(sublista)
print(longitud_total)  # Salida: 9 (3 elementos en cada sublista)


#Métodos útiles para listas anidadas
#______________________________________________________________________________________________________________________________________
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Agregar una nueva sublista al final de la lista anidada
#______________________________________________________________________________________________________________________________________
lista_anidada.append([10, 11, 12])
print(lista_anidada)
# Salida: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# Extender la lista anidada con otra lista
#______________________________________________________________________________________________________________________________________
lista_anidada.extend([[13, 14, 15], [16, 17, 18]])
print(lista_anidada)
# Salida: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

# Eliminar el último elemento de la lista anidada
#______________________________________________________________________________________________________________________________________
lista_anidada.pop()
print(lista_anidada)
# Salida: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

#Creando listas de listas en Python usando for
#______________________________________________________________________________________________________________________________________
lista2 = []
for i in range(2):
	lista2.append([])
	for j in range(3):
		lista2[i].append(0)	
print (lista2)

