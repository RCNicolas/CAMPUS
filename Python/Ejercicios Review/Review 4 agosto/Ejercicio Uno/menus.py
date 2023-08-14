# empleados = {"ID empleado":{"nombre": xxxx,
#                             "telefono": xxxx,
#                             "estado": xxxx,
#                             "entrada": xxx,
#                             "salida": xxxx}}

import workers
import validations

def menu_modify():
    
    while True:
        print("-----------------------")
        print("------Menu modify------")
        print("-----------------------")
        print("1. Modificar nombre    ")
        print("2. Modificar telefono  ")
        print("3. Menu pricipal       ")
        print("-----------------------")
        opcion = validations.validate_variable_type("Ingrese la opcioon deseada\n", "int")
        if opcion >= 1 and opcion <= 4:
            break
        else:
            print("Opcion invalida ")
    return opcion

def menu_principal():

    while True:
        
        print("-------------------------")
        print("     Menu Pincipal       ")
        print("-------------------------")
        print("1. Registrar empleados   ")
        print("2. Listar empleados      ")
        print("3. Modifiar empleados    ")
        print("4. Despedir empleados    ")
        print("5. Entrada/Salida        ")
        print("6. Exit                  ")
        print("-------------------------")
        opcion = validations.validate_variable_type("Ingrese la opcion deseada:  ", "int")
       

        if opcion==1:            
            workers.register()
        elif opcion==2:
            workers.list()
        elif opcion==3:
            workers.modify()
        elif opcion==4:
            workers.dismiss()
        elif opcion==5:
            workers.in_out()
        elif opcion==6:
            print("Saliendo....")
            break
        else:
            print("Opcion invalida...")