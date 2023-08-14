"""60 puntos)Dada la siguiente estructura de datos:

campus = {

"Sputnik": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 35},

"Artemis": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

"Apollo": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

"Houston": {"activity": "teachers room", "students access": False, "schedule": "when teachers need", "capacity": 6},

"Review": {"activity": "skills review", "students access": True, "schedule": "24/7", "capacity": 100}

}
Crea un menú (10 puntos) que se repita hasta que el usuario ingrese la opción de salida (a tu elección) y utilice 
una función para cada opción válida. Las funcionalidades son:

    Mostrar a cuales espacios tienen acceso los campers (10 puntos)
    Mostrar como camper donde puedo estar, si NO es horario de clases (10 puntos) 
    Mostrar donde no puedo sentarme a estudiar nunca como camper (10 puntos)
    Mostrar el promedio de la capacidad de los espacios destinados a clase (10 puntos)

Usar correctamente las excepciones (10 puntos) en este ejercicio."""
opcion =0
campus = {
"Sputnik": {"activity": "classes", 
            "students access": True, 
            "schedule": "6 am to 10 pm", 
            "capacity": 35},
"Artemis": {"activity": "classes", 
            "students access": True, 
            "schedule": "6 am to 10 pm", 
            "capacity": 30},
"Apollo": {"activity": "classes", 
           "students access": True, 
           "schedule": "6 am to 10 pm", 
           "capacity": 30},
"Houston": {"activity": "teachers room", 
            "students access": False, 
            "schedule": "when teachers need", 
            "capacity": 6},
"Review": {"activity": "skills review", 
           "students access": True, 
           "schedule": "24/7", 
           "capacity": 100}
}

def acceso(campus):
    acces=[]
    for espacios in campus.keys():
        if campus[espacios]["students access"] == True:
            acces.append(espacios)
    print(f"\nLos campers tienen acceso a: {acces}")

def no_acceso(campus):
    no_acces=[]
    for espacios in campus.keys():
        if campus[espacios]["students access"] == True and campus[espacios]["schedule"] == "24/7":
            no_acces.append(espacios)
    print(f"\nLos campers tienen acceso a {no_acces} en horaios fuera de clase ")    

def no_acceso_nunca(campus):
    not_acces_never=[]
    for espacios in campus.keys():
        if campus[espacios]["students access"] == False:
            not_acces_never.append(espacios)
    print(f"\nLos campers NO tienen acceso a: {not_acces_never}")


def promedio(campus):
    suma    = 0
    cantidad = 0
    for espacios in campus.keys():
        if campus[espacios]["students access"] == True:
            cantidad += 1
            suma += campus[espacios]["capacity"]
    promedio = suma / cantidad 
    print(f"\nEl promedio de capacidad para los espacios destinados a los campers es: {promedio}")
while True:
    print("""
|===================================================|
|==                  Menu CAMPUS                  ==|
|===================================================|
|== 1. Mostrar espacios de acceso a los campers   ==|
|== 2. Mostrar espacios dispponibles a campers    ==|
|==    fuera del horario de clases                ==|  
|== 3. Mostras lugares donde el camper no puede   ==|
|==    estudiar                                   ==|
|== 4. Mostrar el promedio de la capacidad de     ==|
|==    los espacios destinados a clase            ==|
|==  5. Salir                                     ==|
|===================================================|
""")
    while True:
        try:
            opcion = int(input("Ingrese la opcion deseada: "))
            break
        except TypeError:
            print("Ingresaste una opcion invalida")
        except Exception:
            print("Ingresaste una opcion invalida")

    if opcion == 1:
        acceso(campus)
    elif opcion == 2:
        no_acceso(campus)
    elif opcion == 3:
        no_acceso_nunca(campus)
    elif opcion == 4:
        promedio(campus)
    elif opcion == 5:
        print("Saliendo...")
        break
    else:
        print("Ingeso una opcion invalida ")
        