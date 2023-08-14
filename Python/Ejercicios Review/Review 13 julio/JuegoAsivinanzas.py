import random

numero = random.randint(1,101)

while True:
    intento = int(input("Ingrese un numero: "))
    if intento > numero:
        print("El numero es menor, intentalo otra vez")
    elif intento < numero:
        print("El numero es mayor, intentalo otra vez")
    else: 
        print("Acertaste el numero")
        break