def menu():
    print("""
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
----------AGENDA DE EVENTOS DE AGOSTO------------
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
¬   1. Registrar participantes                  ¬
¬   2. Registrar eventos                        ¬
¬   3. Eliminar registros de participantes      ¬
¬   4. Eliminar/modificar eventos               ¬
¬   5. Ver deuda y participantes por cancelar   ¬
¬   6. Registrar aportes                        ¬
¬   7. Salir                                    ¬
¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬         
""")
    while True:
        try:
            opcion = int(input("Ingrese la opcion deseada: "))    
            break
        except ValueError:
            print("El valor ingresado debe ser un entero. ")
    return opcion

def registrar_participantes(participantes):
    
    print("===========================================================")
    confirmar = True
    while confirmar:
        try:

            cantidad = int(input("Ingrese la cantidad de participantes que desea registrar: "))
            if cantidad > 0 and cantidad <= 5:
                confirmar=False
            elif cantidad > 5:
                print("_____________________________________________")
                print("Solo puedes ingresar hasta 5 participantes. ")
            else:
                print("___________________________________")
                print("Ingresa un valor entero positivo. ")
        except ValueError:
            print("__________________________")
            print("Ingresa un valor entero. ")

    for i in range(0,cantidad):
        while True:
            try:            
                nombre = str(input(f"Ingrese el nombre del participante No {i+1}: "))
                break
            except ValueError:
                print("______________________________________________________________________")
                print("Ingreso un dato que no corresponde con lo pedido, intenelo de nuevo. ")
        confirmar = True
        while confirmar:
            try:            
                documento = int(input(f"Ingrese el documento de {nombre}: "))
                if documento in participantes:
                    print("El documento ingresado ya está registrado. ")
                elif documento < 0:
                    print("Ingresa un dato valido")
                else:
                   confirmar = False 
                
            except ValueError:
                print("______________________________________________________________________")
                print("Ingreso un dato que no corresponde con lo pedido, intenelo de nuevo. ")
        confirmar = True
        while confirmar:
            try:            
                edad = int(input(f"Ingrese la edad de {nombre}: "))
                if edad > 1 and edad <100:
                    confirmar = False
                else:
                    print("Ingresa una edad valida. ")
            except ValueError:
                print("______________________________________________________________________")
                print("Ingreso un dato que no corresponde con lo pedido, intenelo de nuevo. ")
        while True:
            try:            
                cargo = str(input(f"Ingrese el cargo de {nombre}: "))
                break
            except ValueError:
                print("______________________________________________________________________")
                print("Ingreso un dato que no corresponde con lo pedido, intenelo de nuevo. ")

        confirmar = True
        
        while confirmar:
            try:            
                aporte = str(input(f"El participante {nombre} aporto los 50.000 COP?\n(s/n)  ")).lower()
                if aporte == "s":
                    aporte = True
                    confirmar = False
                elif aporte == "n":
                    aporte = False
                    confirmar = False
                else:
                    print("__________________")
                    print("Opcion invalida")
                    print("__________________")
            except ValueError:
                print("______________________________________________________________________")
                print("Ingresó un dato que no corresponde con lo pedido, intentelo de nuevo ") 
                print("______________________________________________________________________")

        participantes[documento]={"nombre": nombre,
                                   "edad": edad,
                                   "cargo": cargo,
                                   "aporte": aporte}
    print(participantes)
    return participantes

def registrar_eventos(eventos):
    print("===========================================================")
    confirmar = True
    while confirmar:
        try:

            cantidad = int(input("Ingrese la cantidad de eventos que desea registrar: "))
            if cantidad > 0 and cantidad <= 5:
                confirmar=False
            elif cantidad > 5:
                print("______________________________________")
                print("Solo puedes ingresar hasta 5 eventos. ")
                print("______________________________________")
            else:
                print("______________________________________")
                print("Ingresa un valor entero positivo. ")
                print("______________________________________")
        except ValueError:
            print("__________________________")
            print("Ingresa un valor entero. ")
            print("__________________________")

    for i in range(0,cantidad):
        while True:
            try:            
                evento = str(input(f"Ingrese el nombre del evento No {i+1}: "))
                break
            except ValueError:
                print("_____________________________________________________________________")
                print("Ingresó un dato que no corresponde con lo pedido, intenelo de nuevo .")
                print("_____________________________________________________________________")
        confirmar = True
        while confirmar:
            try:            
                fecha = int(input(f"Ingrese la fecha para el evento {evento}: "))
                if fecha >0 and fecha <=31:
                    confirmar = False
                else:
                    print("Agosto tiene 31 dias, no mas, ni menos, ingresa una fecha en ese rango. ")
                
            except ValueError:
                print("_____________________________________________________________________")
                print("Ingresó un dato que no corresponde con lo pedido, intenelo de nuevo. ")
                print("_____________________________________________________________________")
        while True:
            try:            
                lugar = str(input(f"Ingrese el lugar donde se realizara el evento: "))
                break
            except ValueError:
                print("_____________________________________________________________________")
                print("Ingresó un dato que no corresponde con lo pedido, intenelo de nuevo. ")
                print("_____________________________________________________________________")

        eventos[evento]={"fecha": fecha,
                         "lugar": lugar,
                         "realizado": False}
    return eventos

def eliminar_prticipantes(participantes):
    print("===========================================================")
    if len(participantes) > 0:
        while True:
            try:
                eliminar = int(input("Ingrese el documento de la persona que desea eliminar del registro: "))
                break
            except ValueError:
                print("_________________________")
                print("Ingresa un valor entero")
                print("_________________________")
        
        if eliminar in participantes and participantes[eliminar]["aporte"] == False:
            print(f"El participante {participantes[eliminar]['nombre']} fue eliminado con exito")
            del participantes[eliminar]
        elif eliminar not in participantes:
            print(f"ERROR! El documento {eliminar} no está registrado. ")
        else: 
            print(f"La persona que desea eliminar: {participantes[eliminar]['nombre']} no puede ser eliminada")
        return participantes
    else:
        print("===========================================================")
        print("No hay participantes para eliminar. ")

def modificar_participantes(participantes):
    print("===========================================================")
    if len(participantes) > 0:
        
        while True:
            try:
                documetno = int(input("Ingrese el documento del participante que realizo el aporte: "))
                if documetno in participantes and participantes[documetno]["aporte"] == False:
                    participantes[documetno]["aporte"] = True
                elif documetno in participantes and participantes[documetno]["aporte"] == True:
                    print(f"El participante {participantes[documetno]['nombre']} ya realizo el aporte ")
                elif documetno not in participantes:
                    print(f"ERROR! El documento {documetno} no está registrado. ")
                break
            except ValueError:
                print("_________________________")
                print("Ingresa un valor valido")
                print("_________________________")
    else:
        print("===========================================================")
        print("No hay participantes registrados. ")
    print(participantes)

def eliminar_modificar_eventos(eventos):
    print("===========================================================")
    if len(eventos) > 0:
        
        while True:
            try:
                opcion = int(input("\n1. Modificar evento\n2. Eliminar evento\n:  "))
                if opcion != 1 and opcion != 2:
                    print("Error! Ingresa una de las opciones. ")
                else:
                    break
            except ValueError:
                print("_________________________")
                print("Ingresa un valor entero")
                print("_________________________")

        if opcion == 1:
            print("=====================")
            print("Eventos registrados: ")
            for i in eventos:
                print("/",i)
            print("=====================")
            while True:
                try:
                    nombreEvento= str(input("Ingrese el nombre del evento que desea modficar: "))
                    break
                except ValueError:
                    print("_________________________")
                    print("Ingresa un dato valido. ")
                    print("_________________________")

            if nombreEvento in eventos and eventos[nombreEvento]["realizado"] == False:
                while True:
                    try:
                        hacer = int(input("\n1. Modificar fecha\n2. Modificar lugar\n3. Marcar como realizado\n4. Modificar nombre\n: "))
                        if hacer != 1 and hacer != 2 and hacer != 3 and hacer != 4:
                            print("Error! Ingresa una de las opciones. ")
                        else:
                            break
                    except ValueError:
                        print("_________________________")
                        print("Ingresa un dato valido ")
                        print("_________________________")

                if hacer == 1:
                    confirmar = True
                    while confirmar:
                        try:
                            fechaNueva = int(input(f"Ingrese la nueva fecha para el evento {nombreEvento}: "))
                            if fechaNueva >0 and fechaNueva <=30:
                                eventos[nombreEvento]["fecha"] = fechaNueva
                                confirmar = False
                            else:
                                print("Agosto tiene 30 dias, no mas, ni menos, ingresa una fecha en ese rango. ")
                        except ValueError:
                            print("_________________________")
                            print("Ingresa un valor entero")
                            print("_________________________")
                elif hacer == 2:
                    while True:
                        try:
                            lugarNuevo = str(input(f"Ingrese el nuevo luagr para el evento {nombreEvento}: "))
                            eventos[nombreEvento]["lugar"] = lugarNuevo
                            break
                        except ValueError:
                            print("_________________________")
                            print("Ingresa una opcion valida. ")
                            print("_________________________")
                elif hacer == 3:
                    if nombreEvento in eventos and eventos[nombreEvento]["realizado"] == False:
                        eventos[nombreEvento]["realizado"] = True
                        print(f"El envento {nombreEvento} fue registrado como realizado ")
                    elif nombreEvento in eventos and eventos[nombreEvento]["realizado"] == True:
                        print(f"El evento {nombreEvento} ya fue realizado. ")
                    elif nombreEvento in eventos and eventos[nombreEvento]["realizado"] == True:
                        print(f"El evento {nombreEvento} no se puede modificar porque ya fue realizado ")
                elif hacer == 4:
                   
                    if nombreEvento in eventos:
                        while True:
                            try:
                                nombreNuevo= str(input("Ingrese el nuevo nombre para el evento: "))
                                break
                            except ValueError:
                                print("_________________________")
                                print("Ingresa un dato valido. ")
                                print("_________________________")
                        eventos[nombreNuevo]=eventos[nombreEvento]
                        del eventos[nombreEvento]
                        print("Cambio de nombre exitoso!! ")
                    else: 
                        print(f"El evento {nombreEvento} no esta registrado")    
                else: 
                    print("Ingresaste una opcion invalida ")

            elif nombreEvento in eventos and eventos[nombreEvento]["realizado"] == True:
                        print(f"El evento {nombreEvento} ya fue realizado, no puede modificarse ")
            else:
                print(f"El evento {nombreEvento} no está registrado ")
                
        elif opcion == 2:
            print("=====================")
            print("Eventos registrados: ")
            for i in eventos:
                print("/",i)
            print("=====================")
            while True:
                try:
                    nombreEvento= str(input("Ingrese el nombre del evento que desea eliminar: "))
                    break
                except ValueError:
                    print("_________________________")
                    print("Ingresa un dato valido ")
                    print("_________________________")
                
            if nombreEvento in eventos and eventos[nombreEvento]["realizado"] == False:
                print(f"El envento {nombreEvento} fue eliminado. ")
                del eventos[nombreEvento]
            elif nombreEvento in eventos and eventos[nombreEvento]["realizado"] == True:
                print(f"No se puede elimina el evento {nombreEvento} porque ya fue realizado. ")
            elif nombreEvento not in eventos:
                print(f"El evento {nombreEvento} no está registrad. ")
                
        else: 
            print("Ingresaste una opcion fuera de las opciones disponibles ")  
    else:
        print("===============================")
        print("No hay eventos para eliminar. ")   
    return eventos

def deuda(participantes):
    print("===========================================================")
    deuda = 0
    j = 0
    if len(participantes)>0:
        for i in participantes:
            if participantes[i]["aporte"] == False:
                deuda += 50000
                participantes[i]["nombre"]
                print(f"{j+1} {participantes[i]['nombre']}")
            else: 
                continue
            j += 1
        print(f"\nDeuda: {deuda}")    
    else: 
        print("=========================================")
        print("Aun no se han registrado participantes. ")