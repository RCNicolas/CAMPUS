limite = int(input("Ingrese un limite maximo para realizar la busqueda de primos: "))
primos = list()
control = 0
''' 
if limite > 2:
    for i in range(2,limite+1):
        for j in range(2,i):
            if i%j == 0:
                control = 0
        if control == 1:
            primos.append(i)
        control = 1
else: 
    print("no se pueda evaluar el rango")
print(primos) '''

if limite > 2:
    for i in range(2,limite+1):
        isPrimo = True
        for j in range(2,i):
            if i%j == 0:
                isPrimo = False
        if isPrimo:
            primos.append(i)
else: 
    print("no se pueda evaluar el rango")
print(primos)