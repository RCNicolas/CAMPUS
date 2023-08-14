"""3. Escribir un programa que pida al usuario 
un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas."""

numero = int(input("Ingrese un numero "))

for i in range(1,numero):
    if i%2 != 0:
        print(i, end=",")
    