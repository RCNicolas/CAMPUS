"""5. Escribir un programa que 
pida al usuario un número entero y 
muestre por pantalla un triángulo 
rectángulo como el de más abajo, de 
altura el número introducido.

*
**
***
****
*****
"""
numero = int(input("Ingrese un numero "))

for i in range(numero+1):
    print("*" * i)