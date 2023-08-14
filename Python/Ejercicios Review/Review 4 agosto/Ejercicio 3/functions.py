import bankDB
import validations
import random
import datetime

def tarjetas_cliente():
    data = bankDB.cargar_data("tarjet.json")
    clientes = bankDB.cargar_data("client.json")
    numero = validations.variable_type("Ingrese el numero de cedula del cliente.\n> ", "int")
    for i in clientes:
        if i["CC"] == numero:
            print(i["name"])
            

def report():
    data = bankDB.cargar_data("tarjet.json")
    #clientes = bankDB.cargar_data("client.json")
    print("------------------------")
    print("1. Reportar tarjeta ")
    print("2. Borrar reporte ")
    print("------------------------")
    while True:
        opcion = validations.variable_type("Ingrese la opcion deseada\n> ","int")
        if opcion == 1 or opcion == 2:
            break
        else:
            print("------------------------")
            print("Ingrese un numero, 1 o 2")

    numero_tarjeta = validations.variable_type("ingrese el numero de la tarjeta que desea reportar\n> ", "int")
    encontrado = False
    for i in data:
        if i['numero']  == numero_tarjeta:
            encontrado = True
            if opcion == 1:
                if i["reporte"] == False:
                    i["reporte"] = True
                else:
                    print("----------------------------")
                    print("La tarjeta ya esta reportada")
            else:
                if i["reporte"] == True:
                    i["reporte"] = False
                else:
                    print("----------------------------")
                    print("La tarjeta no esta reportada")

    if not encontrado:
        print("------------------------------------------------------------")
        print(f"La tarjeta con numero {numero_tarjeta} no esta registrada. ")
    bankDB.guardar_data("tarjet.json", data)

def delete():
    data = bankDB.cargar_data("tarjet.json")
    numero_tarjeta = validations.variable_type("ingrese el numero de la tarjeta que desea eliminar\n> ", "int")
    encontrado = False
    for i in data:
        if i.get("numero")  == numero_tarjeta:
            encontrado = True
            data.remove(i)
                
    if not encontrado:
        print("------------------------------------------------------------")
        print(f"La tarjeta con numero {numero_tarjeta} no esta registrada. ")
    bankDB.guardar_data("tarjet.json", data)

def modify():
    data = bankDB.cargar_data("tarjet.json")
    #clientes = bankDB.cargar_data("client.json")

    numero_tarjeta = validations.variable_type("ingrese el numero de la tarjeta que desea modificar\n> ", "int")
    encontrado = False
    for i in data:
        if i['numero']  == numero_tarjeta:
            nuevo_numero = validations.variable_type("Ingrese el nuevo numero de la tarjeta\n> ","int")
            i["numero"]= nuevo_numero
            encontrado = True
    if not encontrado:
        print("------------------------------------------------------------")
        print(f"La tarjeta con numero {numero_tarjeta} no esta registrada. ")
    bankDB.guardar_data("tarjet.json", data)

def register():
        
    data = bankDB.cargar_data("tarjet.json")
    clientes = bankDB.cargar_data("client.json")
    cc = validations.variable_type("Ingrese la cedula del cliente \n> ", "int")
   
    salir = True
    while salir:
            for i in clientes:
                if i['CC']  == cc:
                    print("---Tipo de tarjeta---")
                    print("1. Master Card")
                    print("2. Visa")
                    print("3. Express")
                    opcion = validations.variable_type("Ingrese la opcion que desea\n> ", "int")
                    if opcion == 1 or opcion == 2 or opcion == 3:
                        if opcion == 1 :
                            tipo = "Master Card"
                        elif opcion == 2:
                            tipo = "Visa"
                        elif opcion == 3:
                            tipo = "Express"
                    else:
                        print("--------------------------------------")
                        print("Ingrese una opcion valida (del 1 al 3)")
            en_tarjeta = False
            for tarjetas in data:
                if tarjetas["id client"] == cc and tarjetas["tipo"] == tipo:
                    en_tarjeta = True
                    break

            if en_tarjeta:
                print(f"El tipo de tarjeta {tipo} ya esta registraa con la cedula {cc}")
            else:
                numero = validations.variable_type("Ingresa el numero de la tarjeta\n> ", "int")
                fecha_actual = datetime.datetime.now()
                fecha_tarjeta = fecha_nueva = fecha_actual.replace(year=fecha_actual.year + 4)
                # fecha_actual.strftime('%m/%Y')
                ccv = random.randint(100,999)   
                data.append({"numero": numero, 
                                "tipo": tipo, 
                                "fecha": fecha_tarjeta.strftime('%m/%y'),
                                "ccv": ccv,
                                "id client": cc,
                                "reporte": False})
                salir = False
                # if opcion == 1 or opcion == 2 or opcion == 3:
                #     if opcion == 1 :
                #         tipo = "Master Card"
                #         break
                #     elif opcion == 2:
                #         tipo = "Visa"
                #         break
                #     elif opcion == 3:
                #         tipo = "Express"
                #         break
                # else:
                #     print("Ingrese una opcion valida (del 1 al 3)")
            

            
        # else:
        #     print("--------------------------------------")
        #     print(f"La cedula {cc} no esta registrada ")            
    bankDB.guardar_data("tarjet.json", data)

def clientes():
    clientes = bankDB.cargar_data("client.json")
    print("")
    print(clientes)
    nombre = validations.variable_type("Ingrese el nombre del cliente\n> ", "str")
    cc = validations.variable_type('Ingrese la cedula del cliente '+nombre+"\n> ", "int")
    for i in clientes:
        if i['CC']  == cc:
            print("--------------------------------------")
            print(f"La cedula {cc} ya esta registrada ")

        else:
            telefono = validations.variable_type('Ingrese el numero de celular de '+nombre+"\n> ", "int")
            while True:
                sexo = validations.variable_type('Ingrese el genero de '+nombre+" (M/F)\n> ", "str").upper()
                if sexo == "M" or sexo == "F":
                    break
                else:
                    print("Ingresa un dato valido. ")

            clientes.append({"CC": cc,
                            "name": nombre,
                            "phone": telefono,
                            "sexo": sexo})
    bankDB.guardar_data("client.json", clientes)
