# Juego de adivinanzas: Crea un juego de adivinanzas en el que el programa contiene un número (de 1 a 100) a ser 
# adivinado y el jugador tiene que adivinarlo. El programa debe dar pistas al jugador indicando si el número a 
# adivinar es mayor o menor que el número ingresado. Utiliza un bucle while para permitir múltiples intentos del 
# jugador.
import random
num = (random.randint(1,101))

while True:
    intento = int(input("Ingrese un numero "))
    if intento < num:
        print("El numero es mayor ")
    elif intento > num:
        print("El numero es menor ")
    else:
        print("Acertaste el numero, el numero ingresado fue: ", intento, "El numero generado es:" , num)
        break

   


