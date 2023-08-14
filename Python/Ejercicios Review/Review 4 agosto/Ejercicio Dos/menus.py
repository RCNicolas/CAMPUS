import validations
import colors
import functions
def menu_principal():
    while True:
        print("----------------------------------")
        colors.print_bold_and_underline(".          Menu Pincipal         .")
        print("")
        print("- 1. Registrar entrada vehiculo  -")
        print("- 2. Marcar salida               -")
        print("- 3. Historial parqueadero       -")
        print("- 4. Dinero recaudado            -")
        print("- 5. Carros en parqueadero       -")
        print("- 6. Salir                       -")
        print("----------------------------------")

        opcion = validations.validate_variable_type("Ingrese la opcion deseada.\n> ", "int")
        
        if opcion==1:            
            functions.register()
        elif opcion==2:
            functions.exit()
        elif opcion==3:
            functions.historial()
        elif opcion==4:
            functions.recaudo()
        elif opcion==5:
            functions.parqueo()
        elif opcion==6:
            print("Saliendo...")    
            break
        else:
            print("Opcion invalida...")
