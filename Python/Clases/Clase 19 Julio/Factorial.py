factor = int(input("Ingrese un numero entero para calcular su factorial: "))
factorial = 1

for i in range(1,factor+1):
    factorial *= i

print(factorial)