matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matriz)
for i in matriz:
    print(i)
print("=============================================")   
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])
print("=============================================")   
for i in range(len(matriz)):
    for j in matriz[i]:
        print(j)
print("=============================================")        
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print(" ")    

#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================
"""1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una 
lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> 
has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas 
introducidas por el usuario."""

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
notas = list()

for i in asignaturas:
    nota = int(input(f"Ingrese la nota de {i}: "))
    notas.append(nota) 
    
print("+++++++++++++++++++++++++++++++")
for i in range(4):
    print(f"La nota de {asignaturas[i]} es: {notas[i]}")
#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================
"""2. Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por 
comas."""

numeros = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(numeros)-1, 0, -1): #Siempre se debe poner range(len(variable))para poder recorrer la lista 
    print(numeros[i], end=",")

print(numeros[0])
#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================
   
"""3. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una 
lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa 
debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
notas = list()

for i in asignaturas:
    nota = int(input(f"Ingrese la nota de {i}: "))
    notas.append(nota) 

print("+++++++++++++++++++++++++++++++")
print(asignaturas)
print(notas)
print("+++++++++++++++++++++++++++++++")
for nota,asi in zip(notas,asignaturas):
    
    if nota<=30:
        notas.remove(nota)
        asignaturas.remove(asi)
        print(f"La asignatura que debe aproabar es: {asi}")

#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================
"""4. Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
y muestre por pantalla la lista resultante."""

abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for posicion, valor in enumerate(abecedario):
    if posicion%3 ==0:
        print(posicion)
        abecedario.remove(valor)
print(posicion,abecedario) 
#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================
"""5. scribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo"""

palabra = input("Ingrese una palabra para verificar si es palindroma: ")

palabraInvertida = palabra[::-1]

if palabra == palabraInvertida :
    print(f"La palabra {palabra} es palindroma")
else: 
    print(f"La palabra {palabra} no es palindroma")
#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================
"""6. Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal"""

palabra = input("Ingrese una palabra: ")
vocales = ["a","e","i","o","u"]

for vocal in vocales: 
    contador = 0
    for letra in palabra: 
        if letra.lower() == vocal:
            contador += 1
    print(f"La vocal {vocal} aparece {contador} veces")  

#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================
"""7. Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla 
su promedio."""

numeros = input("Ingrese numeros separados por comas: ") #Se solicita al usuario ingresar numeros separados por comas
lista = numeros.split(",")
listaNumeros = []

for numero in lista:
    listaNumeros.append(int(numero))

def promedio (listaNumeros):
    calcularPromedio = sum(listaNumeros) / len(listaNumeros)
    return calcularPromedio

print(f"Estos son los numeros que usted ha ingresado :{listaNumeros}")
print(f"El promedio de los numeros que usted ingreso es {promedio(listaNumeros)}")