import menus
import re
# Definimos una expresión regular que busca números (\d) en el string.
# La expresión ^ asegura que el patrón comienza desde el inicio del string,
# el $ asegura que el patrón termina al final del string.
# El modificador \s permite que haya espacios en el string.
# El modificador * asegura que puede haber cero o más ocurrencias de espacios.
# Comparamos el string de entrada con el patrón utilizando la función match de re.
# Si hay una coincidencia, significa que el string solo contiene letras y espacios, sin números.
# patron = r'^[a-zA-Z\s]*$'

def validate_variable_type(solicitud, tipo="str"):
    #<solicitud> se envia en string el mensaje para pedir el dato al usuario
    #"Ingrese un valor entero" por ejemplo
    #<tipo> va a ser el tipo de dato que queremos validar, 
    #"int">entero, 
    #"float">flotante
    #"strcomple"> string con caracteres especiales, 
    #"str">string sin caracteres especiales y con espacios

    patron = r'^[a-zA-Z\s]*$'   
    while True:
        value = input(solicitud)
        if tipo == "int":
            try:
                value = int(value)
                break
            except ValueError:
                print('\033[91;7mInvalid option...\033[0m')
        elif tipo == "float":
            try:
                value = float(value)
                break
            except ValueError:
                print('\033[91;7mInvalid option...\033[0m')
        elif tipo == "strcomple":
            if value == "" or value == " " or len(value) < 6: #Aquí podría ir cualquier otra validación si es una cadena
                print('\033[91;7mInvalid option...\033[0m')
            else:
                break
        elif tipo == "str":
            if re.match(patron, value):
                break
            else:
                print('\033[91;7mInvalid option...\033[0m')
    return value

''' def validate_field(solicitud, isNumeric=False, isFloat=False ):     
    while True:
        value = input(solicitud)
        if isNumeric:
            try:
                value = int(value)
                break
            except ValueError:
                print('\033[91;7mInvalid option...\033[0m')
        elif isFloat:
            try:
                value = float(value)
                break
            except ValueError:
                print('\033[91;7mInvalid option...\033[0m')
        else:
            if value == "" or value == " " or len(value) < 4: #Aquí podría ir cualquier otra validación si es una cadena
                print('\033[91;7mInvalid option...\033[0m')
            #elif value.isalpha() == False :
            else:
                #print('\033[91;7mInvalid option...\033[0m')
                break
    return value '''

def confirmacion():
    while True:
        confirmar = input("Esta seguro de querer salir?\n(s/n) ").lower()
        if confirmar == "n":
            menus.menu_principal()
        elif confirmar == "s":
            break
        else: 
            print("Opcion invalida")