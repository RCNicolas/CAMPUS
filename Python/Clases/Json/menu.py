import json

def leer_json():
    with open ("file.json", "r") as file:
        datos = json.load(file)
        return datos

def info_paises():
    datos = leer_json()
    for i in datos.keys():
        print(f" {i}: poblacion: {datos[i]['poblacion']},   moneda: {datos[i]['moneda']},   continente: {datos[i]['continente']},   area: {datos[i]['area']}. ")

def por_pais():
    datos = leer_json()
    for i in datos.keys():
        print(i)
    pais = input("Ingrese un pais: ").lower()
    if pais in datos:
        print(f"poblacion: {datos[pais]['poblacion']},   moneda: {datos[pais]['moneda']},   continente: {datos[pais]['continente']},   area: {datos[pais]['area']}. ")
    else:
        print(f"El pais {pais} no esta registrado ")


def mayor_poblacion():
    datos = leer_json()
    mayor = 0
    for i in datos.keys():
        if datos[i]["poblacion"] > mayor:
            mayor = datos[i]["poblacion"]
            pais = i
    print(f"Pais con mayor poblacion: {pais}, con {mayor} habitantes")

def menor_area():
    datos = leer_json()
    menor = 0
    for i in datos.keys():
        if datos[i]["area"] < menor:
            menor = datos[i]["area"]
            pais = i
        else:
            menor = datos[i]["area"]

    print(f"Pais con menor area: {pais}, con {datos[pais]['area']} Km^2")

def continente():
    datos = leer_json()
    continente = []
    for i in datos.keys():
        if datos[i]['continente'] != datos[i+1]['continente']:
            continente.append(datos[i]['continente'])
    print(continente)

def menu():
    while True: 
        try:
            opcion= 0
            print("---------------------------------")
            print("     Menu     ")
            print("1. Info de todos los paises ")
            print("2. Info por pais ")
            print("3. Pais con mayor poblacion  ")
            print("4. Pais con menor area ")
            print("5. Continente y sus paises ")
            print("6. Salir ")
            print("---------------------------------")
            opcion = int(input("ingrese la opcion deseada: "))
        except ValueError:
            print("ERROR!!!!!!!!!")

        if opcion == 1:
            print("opcion 1")
            info_paises() 
        elif opcion == 2:
            print("opcion 2")
            por_pais()
        elif opcion == 3:
            print("opcion 3")
            mayor_poblacion()
        elif opcion == 4:
            print("opcion 4")
            menor_area()
        elif opcion == 5:
            continente()

        if opcion == 6:
            break