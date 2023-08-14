"""1. Escribir una función que reciba un número entero positivo y devuelva su factorial."""
def funcion():
    numero = int(input("Ingrese un número entero positivo: "))
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    print(f"El factorial de {numero} es {factorial}")

funcion()    