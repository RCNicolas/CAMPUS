import validations 
import functions


def menu_tarjetas():
    while True:
        print("---------------------")
        print(" Menu Tarjetas ")
        print("---------------------")
        print("1. Añadir tarjeta")
        print("2. Modificar tarjeta")
        print("3. Eliminar tarjeta")
        print("4. Reportes ")
        print("5. Salir. ")
        print("---------------------")

        opcion = validations.variable_type("Ingrese la opcion deseada\n> ", "int")

        if opcion ==1:            
            functions.register()
        elif opcion==2:
            functions.modify()
        elif opcion==3:
            functions.delete()
        elif opcion==4:
            functions.report()
        elif opcion==5:
            print("Saliendo....")
            break
        else:
            print("Opcion invalida...")

def menu_principal():
    while True:
        print("---------------------------------------")
        print(".             Menu Pincipal           .")
        print("---------------------------------------")
        print("- 1. Administar clientes              -")
        print("- 2. Administrar tarjetas             -")
        print("- 3. Consultar tarjetas del cliennte  -")
        print("- 4. Informacion tarjetas             -")
        print("- 5. Listar tarjetas                  -")
        print("- 6. Listar clientes con tarjetas     -")
        print("- 7. Consultar cantidad de tarjetas   -")
        print("- 8. Salir                            -")
        print("---------------------------------------")

        opcion = validations.variable_type("Ingrese la opcion deseada.\n> ", "int")
        
        if opcion==1:            
            functions.clientes()
        elif opcion==2:
            menu_tarjetas()
        elif opcion==3:
            functions.tarjetas_cliente()
        elif opcion==4:
            print("4")
        elif opcion==5:
            print("5")
        elif opcion==6:
            print("6")
        elif opcion == 7:
            print("7")
        elif opcion == 8:
            print("Saliendo...")    
            break
        else:
            print("Opcion invalida...")
