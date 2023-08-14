import modulos
def confirmacion():
    while True:
        confirmar = input("Esta seguro de querer salir?\n(s/n) ").lower()
        if confirmar == "n":
            modulos.menu()
        elif confirmar == "s":
            break
        else: 
            print("Opcion invalida")

def validate_field(value, isNumeric):
    response = True    
    if isNumeric:
        try:
            int(value)
        except ValueError:
            response = False
    else:
        if value == "" or value == " " or len(value) < 4: #Aquí podría ir cualquier otra validación si es una cadena
            response = False
    return response

def validate_file(file_name):
    response = False
    try:
        with open(file_name, "r") as file:
            response = True
    except FileNotFoundError:
        with open(file_name, "x"):
            response = True
    except Exception:
        print("Error al manejar el archivo")
    return response   