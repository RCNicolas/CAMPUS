import users
import events
from validations import confirm

def users_menu():
    while True:
        print("**************************************************")
        print("1. Registrar participante")
        print("2. Eliminar participante")
        print("3. Registrar pago")
        print("4. Volver al menu")
        try:
            option = int(input("Ingrese la opción deseada: "))
        except ValueError:
            print("Ingrese un valor numerico!")
        else:
            if option == 1:
                users.create()
            elif option == 2:
                users.remove_user()
            elif option == 3:
                users.pay_register()
            elif option == 4:
                break
            else:
                print("Ingrese una opcion valida!")
                
def events_menu():
    while True:
        print("**************************************************")
        print("1. Registrar eventos")
        print("2. Modificar eventos")
        print("3. Eliminar eventos")
        print("4. Marcar eventos realizados")
        print("5. Volver al menu")
        try:
            option = int(input("Ingrese la opción deseada: "))
        except ValueError:
            print("Ingrese un valor numerico!")
        else:
            if option == 1:
                events.create()
            elif option == 2:
                events.update()
            elif option == 3:
                events.delete()
            elif option == 4:
                events.change_is_done()
            elif option == 5:
                break
            else:
                print("Ingrese una opcion valida!")

def reports_menu():
    while True:
        print("**************************************************")
        print("1. Saber cantidad de personas en mora y la deuda")
        print("2. Listar participantes en mora")
        print("3. Volver al menu")
        try:
            option = int(input("Ingrese la opción deseada: "))
        except ValueError:
            print("Ingrese un valor numerico!")
        else:
            if option == 1:
                print("opcion 1")
            elif option == 2:
                print("opcion 2")
            elif option == 3:
                break
            else:
                print("Ingrese una opcion valida!")

def main_menu():
    while True:
        print("**************************************************")
        print("Bienvenido, ingrese:")
        print("1. Gestionar participantes/empleados")
        print("2. Gestionar eventos")
        print("3. Informes")
        print("4. salir")
        try:
            option = int(input("Ingrese la opción deseada: "))
        except ValueError:
            print("Ingrese un valor numerico!")
        else:
            if option == 1:
                users_menu()
            elif option == 2:
                events_menu()
            elif option == 3:
                reports_menu()
            elif option == 4:
                if confirm():
                    print("Saliendo!!")
                    break
            else:
                print("Ingrese una opcion valida!")