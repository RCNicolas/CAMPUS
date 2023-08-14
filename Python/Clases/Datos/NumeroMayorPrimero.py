cant = int(input("Digite la cantidad de numeros que va a ingresar: "))
primero = 0
for i in range(1,cant+1):
    if primero == 0:
        primero = int(input("Ingrese el primer numero: "))
    else: 
        numero = int(input("Ingrese otro el siguiente numero: "))
        if numero<primero:
            print(f"El numero ingresado no es mayor al primer numero registrado: ")

 

