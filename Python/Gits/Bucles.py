"""1. Escribe un programa que genere los primeros 4 números perfectos. Un número perfecto es un número entero 
positivo que es igual a la suma de sus divisores propios positivos. Dicho de otra forma, un número perfecto 
es aquel que es amigo de sí mismo. Así, 6 es un número perfecto porque sus divisores propios positivos son 
1, 2 y 3; y 6 = 1 + 2 + 3."""

numeros_perfectos = []
num = 1

while len(numeros_perfectos) < 4:
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    if num == suma:
        numeros_perfectos.append(num)
    num += 1

print("Los primeros 4 números perfectos son:")

print(numeros_perfectos)

#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================
#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================

"""2. Dada la siguiente estructura de datos:

Empresas = {

"Empresa 1": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 
4}, {"departamento": "Ventas", "empleados": 10}, {"departamento": "Operaciones", "empleados": 25}],

"Empresa 2": [{"departamento": "Recursos Humanos", "empleados": 10}, {"departamento": "Contabilidad", "empleados": 
15}, {"departamento": "Ventas", "empleados": 25}, {"departamento": "Operaciones", "empleados": 41}],

"Empresa 3": [{"departamento": "Recursos Humanos", "empleados": 8}, {"departamento": "Contabilidad", "empleados": 
20}, {"departamento": "Ventas", "empleados": 32}, {"departamento": "Operaciones", "empleados": 56}],

"Empresa 4": [{"departamento": "Recursos Humanos", "empleados": 5}, {"departamento": "Contabilidad", "empleados": 
8}, {"departamento": "Ventas", "empleados": 15}, {"departamento": "Operaciones", "empleados": 29}],

"Empresa 5": [{"departamento": "Recursos Humanos", "empleados": 20}, {"departamento": "Contabilidad", "empleados": 
35}, {"departamento": "Ventas", "empleados": 58}, {"departamento": "Operaciones", "empleados": 97}],

}
Crea un menú que se repita hasta que el usuario ingrese la opción de salida (a tu elección) y utilice una función 
para cada opción válida. Las funcionalidades son:

    Mostrar cuántas empresas tienen más de 10 empleados en Recursos Humanos
    Mostrar el promedio de empleados por departamento (teniendo en cuenta todas las empresas para cada calculo)
    Mostrar cuántas empresas tienen el doble o más del doble de empleados en operaciones con respecto a ventas
    Mostrar una nueva estructura de datos reorganizada donde las llaves del diccionario principal no sea empresas 
    sino por departamento."""

estructura_empresas = {

"Empresa 1": [  {"departamento": "Recursos Humanos",
                "empleados": 5},
                {"departamento": "Contabilidad",
                "empleados": 4},
                {"departamento": "Ventas",
                "empleados": 10},
                {"departamento": "Operaciones",
                "empleados": 25}],

"Empresa 2": [  {"departamento": "Recursos Humanos", 
                "empleados": 10}, 
                {"departamento": "Contabilidad", 
                "empleados": 15}, 
                {"departamento": "Ventas", 
                "empleados": 25}, 
                {"departamento": "Operaciones", 
                "empleados": 41}],

"Empresa 3": [  {"departamento": "Recursos Humanos", 
                "empleados": 8}, 
                {"departamento": "Contabilidad", 
                "empleados": 20}, 
                {"departamento": "Ventas", 
                "empleados": 32}, 
                {"departamento": "Operaciones", 
                "empleados": 56}],

"Empresa 4": [  {"departamento": "Recursos Humanos", 
                "empleados": 5}, 
                {"departamento": "Contabilidad", 
                "empleados": 8}, 
                {"departamento": "Ventas", 
                "empleados": 15}, 
                {"departamento": "Operaciones", 
                "empleados": 29}],

"Empresa 5": [  {"departamento": "Recursos Humanos", 
                "empleados": 20}, 
                {"departamento": "Contabilidad", 
                "empleados": 35}, 
                {"departamento": "Ventas", 
                "empleados": 58}, 
                {"departamento": "Operaciones", 
                "empleados": 97}]
}

menu = """
        Menu
(1). Mostrar empresas con más de 10 empleados en Recursos Humanos 
(2). Mostrar el promedio de empleados por departamento
(3). Mostrar empresas con el doble o más del doble de empleados en operaciones con respecto a ventas
(4). Mostar estructura reorganizada por departamentos.
(5). Salir 
Ingrese la opcion deseada: """

def empresa_mas_de_diez(estructura_empresas):
    cont = 0
    for empresa in estructura_empresas.keys():
        for j in estructura_empresas[empresa]:
            if j["departamento"] == "Recursos Humanos":
                if j["empleados"] > 10:
                    cont += 1
    print(cont, "Empresas tienen mas de 10 empledos en recursos humanos ")                    

def mostara_promedio(estructura_empresas):
    
    acumulador_Rh = 0
    acumulador_Cont = 0
    acumulador_ven = 0
    acumulador_ope = 0

    for empresa in estructura_empresas.keys():
        for i in estructura_empresas[empresa]:
            if i["departamento"] ==  "Recursos Humanos":
                acumulador_Rh += i["empleados"]
            elif i["departamento"] ==  "Contabilidad":
                acumulador_Cont += i["empleados"]
            elif i["departamento"] ==  "Ventas":
                acumulador_ven += i["empleados"]
            elif i["departamento"] ==  "Operaciones":
                acumulador_ope += i["empleados"]

    print("El promedio de empleados en Recursos Humanos es: ", acumulador_Rh/5)
    print("El promedio de empleados en Contabilidad es: ", acumulador_Cont/5)
    print("El promedio de empleados en Ventas es: ", acumulador_ven/5)
    print("El promedio de empleados en Operaciones es: ", acumulador_ope/5)

def mostrar_doble(estructura_empresas):
    print("opcion 3")
    for i in estructura_empresas.keys():
        empleados_ven= 0
        empleados_ope =0
        for j in estructura_empresas[i]:
            if j["departamento"] ==  "Ventas":
                empleados_ven = j["empleados"]
            elif j["departamento"] ==  "Operaciones":
                empleados_ope = j["empleados"]
        if empleados_ope >= (empleados_ven*2):
            print(f"La {i} cumple con el requisito ")

def estructura_reorganizada(estructura_empresas):
    print("opcion 4")
    departamento = []
    reestructura = {}
    for j in estructura_empresas["Empresa 1"]:
        departamento.append(j["departamento"])

    for i in departamento:
        reestructura[i]=[]
    
    for i in estructura_empresas.keys(): # i contiene el nombre de la empresa 
        for j in estructura_empresas[i]: # j es una lista que contiene la info de todos los departamentos por empresa
            temporal = {}
            temporal[i] = j["empleados"]
            reestructura[j["departamento"]].append(temporal)
    print(reestructura)

while True:

    while True:

        try:
            opcion=int(input(menu))
            break
        except ValueError:
            print("Ingresó un dato invalido")
    
    if opcion == 1 : 
        empresa_mas_de_diez(estructura_empresas)
    elif opcion ==2  :
        mostara_promedio(estructura_empresas)
    elif opcion == 3 :
        mostrar_doble(estructura_empresas)
    elif opcion == 4 :
        estructura_reorganizada(estructura_empresas)
    elif opcion == 5 :
        print("Saliendo...")
        break
    else:
        print("\nIngrese una opcion valida: ")

#_____________________________________________________________________________________________________________________________________
#=====================================================================================================================================        