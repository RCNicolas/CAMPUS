"""1. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el 
diccionario."""

dic = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

divisa = input("Ingrese su disiva: ")

if divisa in dic.values():
    print(divisa)
else: 
    print(f"La divisa ingresada {divisa} no fue entontrada en el arreglo")
#=====================================================================================================================================
"""2 .Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un 
diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su 
número de teléfono es <teléfono>."""

dic = {"nombre": 0, "edad": 0, "direccion": 0, "telefono": 0}

for i in dic.keys():
    dic[i] = input(f"Ingrese su {i}: ")

print(f"{dic['nombre']} tine {dic['edad']} años, vive en {dic['direccion']} y su numero de telefono es: {dic['telefono']}")
#=====================================================================================================================================
"""3. Escribir un programa que guarde en un diccionario los precios de las verduras de la tabla, pregunte al 
usuario por una verdura, un número de kilos y muestre por pantalla el precio a pagar. Si la fruta no está en 
el diccionario debe mostrar un mensaje informando de ello.

Verdura               Precio (Kg)
Brócoli                2500 COP
Pimentón               1250 COP
Arveja                 3500 COP"""

dic = {"verdura": ["Brócoli", "Pimentón", "Arveja" ],
       "precio": [2500, 1250, 3500]}

verdura = input("Que verdura desea comprar? ")
cantidad = int(input("Cuantos kg desea comprar? "))
precioFinal = 0
j = 0

if verdura in dic["verdura"]:
    for i in dic["verdura"]:
        if verdura == i:
            precioFinal = cantidad*dic["precio"][j]
            print(f"El precio por {cantidad}Kg de {verdura} es: {precioFinal}")    
        j += 1
else:
    print(f"No hay {verdura} disponible")
#=====================================================================================================================================
"""4. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por 
ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se 
añada un nuevo dato debe imprimirse el contenido del diccionario."""

dic = {}

dic["nombre"] = input("Ingrese su nombre: ")
print(dic)
dic["edad"] = input("Ingrese su edad: ")
print(dic)
dic["sexo"] = input("Ingrese su sexo: ")
print(dic)
dic["telefono"] = input("Ingrese su telefono: ")
print(dic)
dic["correo electronico"] = input("Ingrese su correo electronico: ")
print(dic)
#=====================================================================================================================================
"""5. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar 
el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe 
mostrar por pantalla la lista de la compra y el coste total"""

dic = {"articulo": list(),
       "precio": list()}

while True:

    dic["articulo"]

print(dic)
#=====================================================================================================================================
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
#=====================================================================================================================================
"""7. Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes 
se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro 
diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente 
tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una 
opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos 
los clientes, (5) Listar clientes preferentes, (6) Terminar. 

En función de la opción elegida el programa tendrá que hacer lo siguiente: 

1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos. 
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos. 
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre. 
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa
"""

import os
base_datos = {}
def agregarCiente(base_datos):
    continuar = True
    while continuar:

        try:
            nif = int(input("\nIngrese el NIF del cliente: "))
            
            if nif in base_datos:
                print(f"El NIF ingresado ya está registrado y pertenece a {base_datos[nif]['nombre']}.")                    
            else:
                continuar = False  
        except Exception:
            print("Ocurrio un error ingresando los datos ")                
    
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input(f"Ingrese la direccion del cliente {nombre}: ")
    while True:
        try:
            telefono = int(input(f"Ingrese el numero de telefono del cliente {nombre}: "))
            break
        except ValueError:
            print("Opcion no valida")
            
    correo = input(f"Ingrese el correo del cliente {nombre}: ")
    preferencia = input(f"El cliente {nombre} es preferente? \n(s/n)  ").lower()

    if preferencia == "s":
        preferente = True
    elif preferencia == "n":
        preferente = False
    else: 
        print("\nOpcion invalida")

    base_datos[nif]={
        "nombre": nombre,
        "dirrecion": direccion,
        "telefono": telefono,
        "correo": correo,
        "preferente": preferente
    }
    print("\nCliente registrado con exito ")

def eliminarCliente(base_datos):

    if len(base_datos) != 0:    
        confirmar=True
        while confirmar:     
            nif = int(input("\nIngrese el NIF del cliente que desea eliminar: "))
            if nif in base_datos:
                confirmar=input(f"El cliente que desea eliminar es: {base_datos[nif]['nombre']} \nEsta seguro de eliminarlo? (s/n) ").lower()
                if confirmar == "s":
                    print(f"El cliente {base_datos[nif]['nombre']} ha sido eliminado con exito ")
                    del base_datos[nif]
                    confirmar = False
                elif confirmar == "n":
                    print("_____________________________________")
                    confirmarDos=input("\nDesea eliminar otro cliente o salir de la opcion 'eliminar cliente' ?\nPara salir de la opcion eliminar cliente presion 1\nPara eliminar un cliente presiona cualquier tecla \n")
                    if confirmarDos == "1":
                        confirmar = False
                    else: 
                        continue                
                else:
                    print("Opcion no valida ")        
            else:
                print(f"\nEl NIF {nif} no esta registrado")
    else:
        print("\nNo hay clientes registrados para eliminar ")                

def mostrarClientes(base_datos):
    
    if len(base_datos) != 0:
        confirmar = True
        while confirmar:     
            nif = int(input("\nIngrese el NIF del cliente que desea mostrar: "))
            if nif in base_datos:
                print("_____________________________________________________________________")
                print(f"El cliente {base_datos[nif]['nombre']} tiene los suiguientes datos: ")
                print(f"NIF: {nif}" )
                print("Direccion:", base_datos[nif]["dirrecion"])
                print("Correo: ", base_datos[nif]["correo"])
                print("Telefono: ", base_datos[nif]["telefono"])
                confirmar = False
            else:
                print(f"\nEl NIF {nif} no esta registrado")
    else:
        print("\nNo hay clientes registrados para mostrar ")

def listarClientes(base_datos):
    
    if len(base_datos) != 0:
        print("\nClientes registrados: ")
        print("___________________________")
        j = 1
        for i in base_datos.keys():
            print(f"{base_datos[i]['nombre']} ")
            j += 1
    else:
        print("\nNo hay clientes registrados para listar ")

def listarClientesPreferentes(base_datos):
    
    if len(base_datos) != 0:

        hay_preferentes = False
        for cliente in base_datos.values():
            if cliente.get("preferente"):
                hay_preferentes = True
                break

        if hay_preferentes:
            print("\nClientes Preferentes: ")
            print("_______________________")
            for nif, cliente in base_datos.items():
                if cliente["preferente"]:
                    print("Cliente: ", cliente["nombre"] ," NIF: ", nif)
        else:
            print("\nNo hay clientes preferentes en la base de datos.")
        
    else:
        print("\nNo hay clientes registrados en la base de datos para mostrar ")            

menu = """
____________________________________
        Menu base de datos        __
------------------------------------
(1) Añadir cliente                --
(2) Eliminar cliente              -- 
(3) Mostrar cliente               --
(4) Lista todos los clientes      --
(5) Listar clientes preferentes   --
(6) Terminar                      --
------------------------------------
Ingrese una opcion: """                    
mostrarMenu = "s"

while mostrarMenu != "n":

    if mostrarMenu == "s":
        while True:
            try:
                opcion = int(input(menu))
                break
            except ValueError:
                os.system("clear")
                print("Opcion no valida")
    elif mostrarMenu == "n": 
        break
    else:
        print("Opcion no valida ")
        break
    os.system("clear")
    if opcion == 1:
        agregarCiente(base_datos)
        mostrarMenu = input("\nDesea ver el menu de nuevo?\nSi presiona: (s)\nNo, cerar programa presiona cualquier tecla ").lower()
    elif opcion == 2:
        eliminarCliente(base_datos)
        mostrarMenu = input("\nDesea ver el menu de nuevo?\nSi presiona: (s)\nNo, cerar programa presiona cualquier tecla ").lower()
    elif opcion == 3:
        mostrarClientes(base_datos)
        mostrarMenu = input("\nDesea ver el menu de nuevo?\nSi presiona: (s)\nNo, cerar programa presiona cualquier tecla ").lower()
    elif opcion == 4:
        listarClientes(base_datos)
        mostrarMenu = input("\nDesea ver el menu de nuevo?\nSi presiona: (s)\nNo, cerar programa presiona cualquier tecla ").lower()
    elif opcion == 5:
        listarClientesPreferentes(base_datos)
        mostrarMenu = input("\nDesea ver el menu de nuevo?\nSi presiona: (s)\nNo, cerar programa presiona cualquier tecla ").lower()
    elif opcion == 6:
        print ("Saliendo... ")
        break
    else:
        print ("opcion invalida")
#=====================================================================================================================================