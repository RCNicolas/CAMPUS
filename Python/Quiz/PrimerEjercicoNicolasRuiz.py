# ''' #     Escriba un programa en Python que encuentre todos los pares de números primos gemelos en un rango dado.
# #     El programa debe solicitar al usuario que ingrese el límite superior del rango de búsqueda.
# #     Luego, debe verificar todos los números en el rango (2, límite) para determinar si son números primos y si su diferencia con 
# #     el siguiente número también es primo.
# #     Finalmente, el programa debe imprimir los pares de números primos gemelos encontrados.
# rango = int(input("Ingrese el limite superior del rango de busqueda: "))
# numeroSiguiente = 0

# for i in range(2,rango+1):

#     if i%1 == 0 and i%i == 0 and i%2 !=0:
#         numeroSiguiente = i+2
#         if numeroSiguiente <= rango:
#             print(f"Pares de gemelos primos: ({i}, {numeroSiguiente}) ")
        
limite_superior = int(input("Ingrese el límite superior del rango de búsqueda: "))#Esta linea de codigo pide al usuario que ingrese un rango de busqueda
for num in range(2, limite_superior):#Esta linea de codigo recore el rango desde dos hasta el ingresado por el usuario 
    if num + 2 <= limite_superior:#Esta linea de codigo compara si num +2 es menor o igual al limite ingresado por el usuario
        es_primo_actual = True#Esta linea asigna a la variable es_primo_actual el valor booleano de True
        es_primo_siguiente = True#Esta linea asigna a la variable es_primo_siguiente el valor booleano de True
        for i in range(2, num):#Esta for recorre el 
            if num % i == 0:#esta linea de codigo compara si el numero num es divisible en los valores iterables que toma i. para ver si el numero actual es divisible entre uno o mas numeros y ver que no es primo
                es_primo_actual = False#Esta linea de codigo asigna a la variable es_primo_actual el valor booleano de False si la condicion anterior se cumple
                break#Si la condicion se cumple se cierra la estructura de control
        for j in range(2, (num + 2)):#Esta linea de codigo recoge un rango desde num hasta dos numeros mas, para posteriormente calcular si su numero siguiente con diferencia de dos tambien es primo
            if (num + 2) % j == 0:#esta linea de codigo compara si el numero num +2 es divisible en los valores iterables qeu toma i, esto para verificar si el numerosiguiente que su diferencia sea dos con el primo actual es disivible en uno o msa numeros
                es_primo_siguiente = False#Esta linea de codigo asigna a la variable es_primo_actual el valor booleano de False si la condicion anterior se cumple
                break#Si la condicion se cumple se cierra la estructura de control
        if es_primo_actual and es_primo_siguiente:#Esta linea se codigo verifica si ambas variables tiene el valor booleano de True, de ser asi esta condicion tambine toma el valor de True 
            print(f"({num}, {num + 2}) son números primos gemelos.")#Si se cumple la validacion anterior se imprimen todos los pares de numeros generlos primos encontrados 
           
            