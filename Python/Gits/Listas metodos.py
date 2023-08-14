#=====================================================================================================================================
#======C A D E N A====================================================================================================================
#=====================================================================================================================================
cadena = "Hola,campers,!!"
cadena2 = "Bienvenidos"
cadena3 = "Hola"

#Acceder a un elemento
#______________________________________________________________________________________________________________________________________
print(cadena[3])
print(cadena[-1])

#Subcadenas
#______________________________________________________________________________________________________________________________________
print(cadena[1:6:2])
print(cadena[::-1])
print(cadena[:-2])

#operaciones con cadenas
#______________________________________________________________________________________________________________________________________
print(cadena + " " + cadena2)#+ con cadenas, concatena
print(5 * cadena2)#concatenacion de cadena2 5 veces
print(cadena3 in cadena) #Devuelve True si cadena3 es una cadena contenida en cadena y False en caso contrario.
print(cadena3 not in cadena) #Devuelve True si cadena3 es una cadena no contenida en cadena y False en caso contrario.

#Comparación de cadenas: funciona comparando con el orden establecido en ASCII, https://elcodigoascii.com.ar/
#______________________________________________________________________________________________________________________________________
print(cadena == cadena2) #Devuelve True si cadena es igual que cadena2 y False en caso contrario.
print(cadena > cadena2) #Devuelve True si cadena sucede a la cadena2 y False en caso contrario.
print(cadena < cadena2) #Devuelve True si cadena antecede a la cadena2 y False en caso contrario.
print(cadena >= cadena2) #Devuelve True si cadena sucede o es igual a la cadena2 y False en caso contrario.
print(cadena <= cadena2) #Devuelve True si cadena antecede o es igual a la cadena2 y False en caso contrario.
print(cadena != cadena2) #Devuelve True si cadena es distinta a la cadena2 y False en caso contrario.

#funciones con cadenas
#______________________________________________________________________________________________________________________________________
print(len(cadena3)) # Devuelve el número de caracteres de la cadena
print(min(cadena)) #Devuelve el carácter menor de la cadena
print(max(cadena)) #Devuelve el carácter mayor de la cadena
print(cadena2.title()) #Devuelve la cadena con la primera letra en mayuscula de cada palabra de la cadena
print(cadena2.capitalize()) #Devuelve la cadena con la primera letra en mayuscula 
print(cadena2.upper()) #Devuelve la cadena con los mismos caracteres de la cadena pero en mayúsculas.
print(cadena2.lower()) #Devuelve la cadena con los mismos caracteres de la cadena pero en minúsculas.
print(cadena2.lower()) #Devuelve la cadena con los mismos caracteres de la cadena con el primer carácter en mayúsculas y el resto en minúsculas.
print(cadena.split(",")) #Devuelve la lista formada por las subcadenas que resultan de partir la cadena usando como delimitador la cadena ",". Si no se especifica el delimitador utiliza por defecto el espacio en blanco.
#=====================================================================================================================================
#======L I S T A S====================================================================================================================
#=====================================================================================================================================
lista = ["A","B","C"]
lista2 = [1, 65, 0]
lista3 = ["A", 54, True,54,54, False]

lista4 = list("Python")  #Convertir un string en una lista
print(lista4)

l1 = [1,2,3,4]
l2 = list(l1)#crear lista y copiar listas
l2.append(5)#Agregar al final de las listas un valor 
print(l1)

#Acceso a elementos
#______________________________________________________________________________________________________________________________________
print(lista4[2])

#Sublistas - aplica lo mismo que subcadenas

#funciones que no modifican las listas
#______________________________________________________________________________________________________________________________________
print(len(lista))#Tamaño de una lista
print(max(lista2))#trae el valor maximo siempre y cuando se puedan comparar
print(min(lista2))#trae el valor mínimo siempre que los datos sean comparables.
print(54 in lista3)#Saber si este dato esta en la lista 
print(lista3.count(54))#Contar cuantas veces está un elemento en la lista
print(all(lista3))#validar si todos los datos son verdaderos
print(any(lista3))#validar si algún dato es verdadero
print(lista.index("B"))#Entrega el index o posicion del primer valor encontrado
print(sum(lista2))#Devuelve la suma de los elementos de la lista, siempre que los datos se puedan sumar.

#operaciones que si modifican las listas
#______________________________________________________________________________________________________________________________________
lista2[2] = 35#cambiar un valor respecto a su indice
lista2.sort()#Puedes ordenar los elementos de la lista
lista + lista2 #nueva lista con los elementos de ambas
lista.append("D")#Agregamos nuevo elemento al final
lista.pop()#Elimina el ultimo elemento o elimina un valor respecto al indice que le asignemos
lista.insert(1, "H")#inserto un elemento en una posicion deseada
lista3.remove(54)#Sirve para remover el primer dato con el parametro asignado
lista.clear() #Limpiar la lista
lista.reverse() #Invertir el orden de los elementos de la lista
"""
**Sintaxis:** `lista2.insert(indice, elemento)`
- **`lista`**: Es la lista en la que deseas insertar el elemento.
- **`indice`**: Es el índice donde deseas insertar el nuevo elemento. Los elementos actuales y futuros se desplazarán a la derecha para dejar espacio al nuevo elemento.
- **`elemento`**: Es el valor que deseas insertar en la lista.
"""
#Copia de listas
#______________________________________________________________________________________________________________________________________
lista_nueva = lista #Asocia la la variable l1 la misma lista que tiene asociada la variable l2, es decir, ambas variables apuntan a la misma dirección de memoria. Cualquier cambio que hagamos a través de una afectará a la otra.
nueva_lista = list(lista) #Crea una copia de la lista asociada a l2 en una dirección de memoria diferente y se la asocia a l1. Las variables apuntan a direcciones de memoria diferentes que contienen los mismos datos. Cualquier cambio que hagamos a través de una no afectará a la otra.

#Recorrer listas que contienen listas
#______________________________________________________________________________________________________________________________________
tabla = [[1,2,3],[4,5,6],[7,8,9]]
print(tabla)
for i in range(len(tabla)):
    for j in range(len(tabla[i])):
        print(tabla[i][j], end=" ")
    print(" ")

    