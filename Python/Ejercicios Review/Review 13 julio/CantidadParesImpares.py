cantidadNumeros = int(input("Digite la cantidad de numeros que desea ingresar: "))
negativos = 0
positivos = 0
for i in range(1, cantidadNumeros+1):
    numero = int(input("Ingrese un numero: "))
    if numero < 0:
        negativos += 1
    elif numero == 0:
        print("El numero ingredaso fue cero")
    else:
        positivos += 1

print(f"La cantidad de numeros positivos fue {positivos}")
print(f"La cantidad de numeros negativos fue {negativos}")