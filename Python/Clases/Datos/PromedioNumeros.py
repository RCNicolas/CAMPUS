suma = 0
cont = 0
while True:
    numero = int(input("Ingrese un numero entero positivo, para cerrar el programa ingrese uno negativo"))
    if numero >= 0:
        suma += numero
        cont += 1
    else:
        break

print(f"El promedio de los numeros ingresados es: {suma/cont}")