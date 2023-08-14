"""
Para tributar un determinado impuesto se debe ser mayor de 16 años 
y tener unos ingresos iguales o superiores a 4.000.000 COP mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos 
mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

edad = int(input("Ingrese su ead "))
ingreso = int(input("Ingrese su salario mensual "))

if edad > 16 and ingreso >= 4000000:
    print("El usuario puede tributar")
else:
    print("El usuario no puede tributar")    

