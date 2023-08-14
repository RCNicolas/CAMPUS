edad = int(input("Ingres la edad del cliente "))
    
if edad < 4 and edad > 0:
    print("El cliente entra gratis")
elif edad >= 4 and edad <= 18:
    print("El cliente debe pagar 5.000 COP")
elif edad > 18 and edad <100:
    print("El cliente debe pagar 10.000 COP")
else:
    print("Error! ingreso una edad invalida")
    

    
    