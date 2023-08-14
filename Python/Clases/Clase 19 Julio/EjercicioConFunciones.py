
def suma(numero1, numero2):
    return numero1 + numero2
def resta(numero1, numero2):
    return numero1 - numero2
def multi(numero1, numero2):
    return numero1 * numero2
def div(numero1, numero2):
    return numero1 / numero2
def potencia(numero1, numero2):
    return numero1 ** numero2
def operacion(parametro):
    numero1 = int(input("Ingrese un primer numero: "))
    numero2 = int(input("Ingrese un segundo numero: "))
    return parametro(numero1, numero2)
continuar = True

while continuar:
    print("============================")
    opcion = (input("    Menu\n 1.Suma\n 2.Resta\n 3.Multiplicacion\n 4.Divisicion\n 5.Potencia\n 0.Salir \n"))
    print("============================")
    
    if opcion == "1":
        print("El resultado de la suma es:" ,operacion(suma))
    elif opcion == "2":
        print(f"El resultado de la resta es: {operacion(resta)}")
    elif opcion == "3":
        print(f"El resultado de la multiplicaion es: {operacion(multi)}")
    elif opcion == "4":
        print(f"El resultado de la division es: {operacion(div)}")
    elif opcion == "5":
        print(f"El resultado de la potencia es: {operacion(potencia)}")
    elif opcion == "0":
        continuar = False
    else: 
        print("Opcion no valida")
        
    