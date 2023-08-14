# participantes = {
#     "1234567890":{"name":"Juan Mariño", "age": 55, "area": "operations", "is paid": False},
#     "1234567890":{"name":"Juan Mariño", "age": 55, "area": "operations", "is paid": False},
#     "1234567890":{"name":"Juan Mariño", "age": 55, "area": "operations", "is paid": False}
# }
import validations
import usersBD

def create():
    users = usersBD.cargar("users.txt")
    print(users)
    while True:
        print("*****************************************************************")
        print("Creación del participante")
        document = input("Ingrese el documento del participante: ")
        if not validations.validate_field(document, False):
            print("Valor no válido")
            continue
        if users.get(document, False) != False:
            print("Usuario ya existente")
            continue
        name = input("Ingrese el nombre del participante: ")
        if not validations.validate_field(name, False):
            print("Valor no válido")
            continue
        age = input("Ingrese la edad: ")
        if not validations.validate_field(age, True):
            print("Valor no válido")
            continue
        area = input("Ingrese el area a la que pertenece el participante: ")
        if not validations.validate_field(area, False):
            print("Valor no válido")
            continue
        option = input("Ingrese s si pagó, o ingrese n si no pagó: ")
        is_paid = validations.validate_payment(option)
        print("*****************************************************************")        
        if document != " ":
            users[document] = {"name": name, "age": age, "area":area, "is paid": is_paid}
            break
    usersBD.guardar(users, "users.txt")        

def remove_user():
    users = usersBD.cargar("users.txt")
    print("*****************************************************************")
    document = input("Ingrese el documento a eliminar: ")
    user = users.get(document, False)
    if user == False:
        print("Usuario no registrado :(")
    elif user["is paid"]:
        print("Ya pagaste, ya perdiste")
    else:
        del users[document]
        print("Usuario eliminado!")    
    print("*****************************************************************")
    usersBD.guardar(users, "users.txt")
    
def pay_register():
    users = usersBD.cargar("users.txt")
    print("*****************************************************************")
    document = input("Ingrese el documento del participante a pagar: ")
    user = users.get(document, False)
    if user == False:
        print("Usuario no registrado :(")
    elif user["is paid"]:
        print("Ya pagaste, no tienes que pagar")
    else:
        users[document]["is paid"] = True
        print("Pagaste!")    
    print("*****************************************************************")
    usersBD.guardar(users, "users.txt")