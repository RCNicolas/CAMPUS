cadena = "Hola, campers,!!"
cadena2 = "Bienvenidos" 
cadena3 = "Hola"
#acceder a un elemento 
print(cadena[3])
print(cadena[13])
print(cadena[-1])

#Subcadenas
print(cadena[1:6])
print(cadena[1:6:2])
print(cadena[::-1])#Invierte la cadena
print(cadena[:-2])

#operaciones con cadenas 
print(cadena + " " + cadena2)
print(2 * cadena2)
print(cadena == cadena2)
print(cadena in cadena3)
print(cadena > cadena3)

#Funciones con cadenas
print(len(cadena3))#tamaño de la cadena
print(cadena2.upper())#pasar la cadena a mayusculas
print(cadena2.lower())#pasar la cadena a minusculas
print(cadena.split(","))#Separala cadena 