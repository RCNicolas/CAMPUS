"""6. Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde 
la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere 
añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su 
coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""

dic = {}
continuar = True
pendiente = 0
cobro = 0
seguir = True
while continuar:
    opcion = int(input("""
=======================
    Sistema de facturas
1. Anadir una factura.
2. Pagar una factura.
3. Salir.
=======================
"""))
    
    if opcion == 1:
        factura = int(input("Ingrese el número de factura: "))
        if factura in dic:
            print("La factura ya existe")
            while continuar:
                factura = int(input("Ingrese el número de factura: "))
                if factura in dic:
                    continuar = True
                else:
                    continuar = False
        else:            
            coste = int(input("Ingrese el coste: "))
            dic[factura] = coste
            cobro += coste
            pendiente = cobro
            print(f"La factura {factura} ha sido registrada con un coste de {coste}")
            print(f"Se ha cobrado en total {cobro}")
        if factura not in dic:
            coste = int(input("Ingrese el coste: "))
            dic[factura] = coste
            cobro += coste
            pendiente = cobro
            print(f"La factura {factura} ha sido registrada con un coste de {coste}")
            print(f"Se ha cobrado en total {cobro}")
            print("Saldo pendiente: ", pendiente)
        continuar = True
    elif opcion == 2 and len(dic) > 0:
        factura = int(input("Ingrese el número de factura: "))
        if factura in dic:
            print(f"La factura {factura} ha sido pagada y eliminada")            
            pendiente -=  dic.pop(factura)
            print("Saldo pendiente: ", pendiente)
        else:
            print("La factura no existe")
            print(f"Facturas registradas: {dic.keys()}")
    elif opcion == 3:
        continuar = False
    else:
        print("Opción no disponible")

print(dic)
print(f"Se ha cobrado un todal de {cobro} por las facturas registradas")
print(f"Hay un saldo pendiente de {pendiente}")
