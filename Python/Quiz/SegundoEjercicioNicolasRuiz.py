# 2. En este ejercicio, el objetivo es encontrar números primos palindrómicos. Un número primo palindrómico es aquel número que es 
# #   primo y que se lee igual de izquierda a derecha y de derecha a izquierda. Por ejemplo, 131 y 757 son números primos palindrómicos.

# # Instrucciones:

# #     Escriban un programa en Python que encuentre todos los números primos palindrómicos en un rango dado.
# #     El programa debe solicitar al usuario que ingrese un número límite para el rango de búsqueda.
# #     Luego, debe verificar todos los números en el rango (10, límite) para determinar si son números primos palindrómicos.
# #     Finalmente, el programa debe imprimir los números primos palindrómicos encontrados.
limite = int(input("Ingrese un número límite para el rango de búsqueda: "))#Esta linea de codigo le pide alusuario que ingrese un limite para realizar la busqueda de los numeros primos 
numeros_palindromicos = []#Se crea una lista indefinida donde se asignaran los numeros palindromos posteriormente 
for num in range(10, limite):#Se itera la variable num desde 10 hasta el limite ingresado por el usuario
    es_primo = True#Secrea una variable con el valor de True para los numeros primos
    for i in range(2, num):#Se ejecita un ciclo desde elnumero 2 hasta el valor actual de num
        if num % i == 0:#Se comprueba si num es divisible entre uno o mas numeros, esto para saber si es primo o no, si es divisible en mas numeros no es primo
            es_primo = False#Al cumplirse la condicion dada anteriormente se asigna el valor de False a la variable es_primo, para indicar que el numero actual no es primo
            break#Al cumplirse la condicion el break cierra la estrctura de control
    if es_primo and str(num) == str(num)[::-1]:#Aca se comprueba que el numero actual sea igual a su inverso para saber si es palindromo, por ejemplo, 242 es palindromo ya que su inverso es igual 242, encambio 123 no es palindromo porque su inverso es diferente 321
        numeros_palindromicos.append(num)#Si se cumple la condicion anterior se agrega el numero a la lista creada anteriormente
print("Números primos palindrómicos encontrados:")#Imprime en consola la frase "Números primos palindrómicos encontrados:"
for num in numeros_palindromicos:#Iteramos la variable num en el arreglo de los palindromos para que tome el valor de cada posicion y poder mostrar acontinuacion los numeros palindromos
    print(num)#Imprime en consola los numeros que son palindromos
