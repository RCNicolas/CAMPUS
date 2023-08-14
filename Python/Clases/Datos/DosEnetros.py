numeroUno = int(input("Ingrese un numero entero: "))
numeroDos = int(input("Ingrese otro numero entero: "))
suma = 0
cont = 0
if numeroUno < numeroDos:
    for i in range(numeroUno, numeroDos+1):
        suma += i
        cont +=1
    print(f"El promedio de la suma de los numeros del {numeroUno} hasta el {numeroDos} es : {suma/cont}")
elif numeroUno > numeroDos:
    for i in range(numeroUno, numeroDos-1, -1):
        suma += i
        cont +=1
    print(f"El promedio de la suma de los numeros del {numeroDos} hasta el {numeroUno} es : {suma/cont}")
elif numeroDos== numeroUno:
    print("Los numeros ingresados son iguales ")