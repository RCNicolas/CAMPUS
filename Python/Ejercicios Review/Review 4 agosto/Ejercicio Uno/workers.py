import workersDB
import validations
import menus
from datetime import datetime

def dismiss():
    workers = workersDB.cargar('workers.json')

    if len(workers) != 0:
        dni = validations.validate_variable_type("Ingrese DNI del empleado que va a despedir\n> ", "int")
        dni = str(dni)
        if workers.get(dni, False) != False:
            workers[dni]['isActive'] = False
            print(f"El empleado {workers[dni]['name']} fue despedido ")
        else:
            print(f"El DNI {dni} no esta registrado ")
        workersDB.guardar('workers.json', workers)
    else:
        print("-----------------------------------------")
        print("No hay empleados registrados en la DB ")

def in_out():
    workers=workersDB.cargar("workers.json")
    linea = []
    if len(workers) != 0:
        dni = validations.validate_variable_type("Ingrese el documento del empleado a registar\n> ", "int")
        dni=str(dni)
        if workers.get(dni, False) != False and workers[dni]["isActive"]:
            linea.append(dni)
            advertencia = ""
            print("--------------------")
            option = validations.validate_variable_type("Ingrese\n1. Para registrar entrada\n2. Para registrar salida\n> ", "int")
            if option == 1 or option ==2:
                time = datetime.now()
                moment = time.strftime("%d-%m-%Y %H:%M")
                hour = time.hour
                minute = time.minute
                linea.append(moment)       

                if option == 1:
                    linea.append("in")
                    if hour > 8:
                        advertencia = "Llegó tarde"
                    elif hour == 8 and minute > 0:
                        advertencia = "Llegó tarde"
                else:
                    linea.append("out")
                    if hour < 18:
                        advertencia = "Salió temprano"
                if advertencia != "":
                    linea.append(advertencia)
                workersDB.guardar_registro("registros.csv", linea)
            else:
                print("Opción no válida")
        elif workers.get(dni, False) != False and workers[dni]["isActive"] == False:
            print("-----------------------------------------")
            print(f"El empleado {workers[dni]['name']} fue despedido ")

        else:
            print("-----------------------------------------")
            print("Empleado no existente!") 
    else:
        print("-----------------------------------------")
        print("No existe registro de empleados en la DB")

def register():
    workers = workersDB.cargar('workers.json')
    print(" ")
    name = validations.validate_variable_type("Ingrese el nombre del trabajador\n> ", "str")

    while True:
        dni = validations.validate_variable_type('Identificación de ' +name+": ", "int")
        if workers.get(dni, False) != False:
            print(f'El DNI {dni} ya esta registrado ')
            continue   
        else:
            break

    phone_number=validations.validate_variable_type('Ingrese el numero de telefono de '+name+": ", "int")
    workers[dni] = {'name': name, 'phone':phone_number, 'isActive': True}
        
    workersDB.guardar('workers.json', workers)
        
def list():
    workers = workersDB.cargar('workers.json')
    
    if len(workers) != 0:
        print("")
        print("------Empleados Registrados-----")
        for i in workers.keys():
            if workers[i]["isActive"]:
                print(f"|| {workers[i]['name']}, DNI: {i} ")
        print(" ")
    else:
        print("-----------------------------------------")
        print("No hay empleados registrados en la DB ")

def modify():
    workers = workersDB.cargar('workers.json')
    print("")
    print("------Empleados Registrados-----")
    if len(workers) != 0:
        
        for i in workers.keys():
            print(f"|| {workers[i]['name']}, DNI: {i} ")
        print("---------------------------------------------------")
        dni = str(validations.validate_variable_type("Ingrese el DNI del empleado que desea modificar\n> ", "int"))
        dni = str(dni)
        while True:
            if dni in workers.keys():
                opcion = menus.menu_modify()
                if opcion == 1:
                    nombre = validations.validate_variable_type("Ingrese el nombre del empleado \n> ", "str")
                    workers[dni]['name'] = nombre
                    workersDB.guardar('workers.json', workers)
                elif opcion == 2:
                    phone_numbre = validations.validate_variable_type("Ingrese el nuevo telefono del empleado\n> ", "int")
                    workers[dni]['phone'] = phone_numbre
                    workersDB.guardar('workers.json', workers)
                elif opcion == 3:
                    break
                else:
                    print('\033[91;7mInvalid option...\033[0m')
            else:
                print(f'El DNI {dni} no esta registrado ')
                break
                
    else:
        print("-----------------------------------------")
        print("No hay empleados registrados en la DB ")
    workersDB.guardar('workers.json', workers)