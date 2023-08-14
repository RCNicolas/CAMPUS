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
        