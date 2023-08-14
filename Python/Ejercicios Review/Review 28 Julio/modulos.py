"""Ejercicio:
La gobernación de Santander están organizando un evento deportivo en el cual se estarán organizando tres 
carreras:
    atletismo
    ciclismo
    patinaje
Para esta organización la gobernación comenzó a recolectar la información de los participantes en 
planillas manualmente, sin esperar que habría demasiada gente interesada y la cantidad de personas 
inscritas fue poco manejable. La gobernación requiere un programa simple hecho en Python que le permita 
recolectar la información de los participantes con los siguientes requerimientos.
La aplicación debe:
-Permitir registrar a los participantes mayores a 18 años y residentes en el departamento de Santander, 
pidiéndole seleccionar una de las tres carreras en la cual participar.
-Marcar en un ranking las 5 primeras posiciones a los participantes de cada carrera.
-No se permite la modificación de la información a los participantes.
-Mantener la información de los participantes registrados aún así la aplicación se finalice (La única 
forma de finalizar debe ser voluntaria del usuario que la utilice).
-Puede tener menús (haciendo la validación de la opción con números y por tanto, validando posibles 
excepciones)y submenús tantos como se requiera siempre y cuando sea ordenado y entendible. 
-Para finalizar la aplicación se debe pedir confirmación
Tener una estructura organizada a nivel de código con módulos y funciones."""
import validacions
import participantesBD


def registrar_participantes():
    participantes = participantesBD.cargar("participantes.txt")
    #BD.guardar(participantes, "participantes.txt")
    print(participantes)
    print("\033[96m===========================================================\033[0m")
   
    confirmar = True
    while confirmar:
        try:
            cantidad = int(input(f"Ingrese la cantidad de participantes que desea registrar: "))
            if cantidad >= 0 and cantidad <= 5:
                confirmar=False
            elif cantidad > 5:
                print("_____________________________________________")
                print("\033[91mSolo puedes ingresar hasta 5 participantes. \033[0m")
            else:
                print("___________________________________")
                print("\033[91mIngresa un valor entero positivo. \033[0m")
        except ValueError:
            print("__________________________")
            print("\033[91mIngresa un valor entero. \033[0m")

    for i in range(0,cantidad):
        while True:
            try:            
                nombre = str(input(f"Ingrese el nombre del participante No {i+1}: "))
                break
            except ValueError:
                print("______________________________________________________________________")
                print("\033[91mIngreso un dato que no corresponde con lo pedido, intenelo de nuevo. \033[0m")

        confirmar = True
        while confirmar:
            try:            
                documento = int(input(f"Ingrese el documento de {nombre}: "))
                    
                if documento in participantes:
                    print("Usuario ya existente")
                    confirmar = True
                else:
                    confirmar = False
                
            except ValueError:
                print("______________________________________________________________________")
                print("\033[91mIngreso un dato que no corresponde con lo pedido, intenelo de nuevo. \033[0m")
        confirmar = True
        while confirmar:
            try:            
                edad = int(input(f"Ingrese la edad de {nombre}: "))
                if edad >= 18 and edad <100:
                    confirmar = False
                elif edad > 0 and edad < 18:
                    print("El participante debe tener 18 años o mas ")
                    break
                else:
                    print("Ingresa una edad valida. ")
            except ValueError:
                print("______________________________________________________________________")
                print("Ingreso un dato que no corresponde con lo pedido, intenelo de nuevo. ")

        if edad < 18:
            print("El participante que desea registrar no puede participar debe ser mayor de 18")
            break

        confirmar = True
        while confirmar:
            try:            
                residente = str(input(f"El participante {nombre} es residente en Santaner\n(s/n)  ")).lower()
                if residente == "s":
                    residente = True
                    confirmar = False
                elif residente == "n":
                    residente = False
                    confirmar = False
                else:
                    print("__________________")
                    print("Opcion invalida")
                    print("__________________")
            except ValueError:
                print("______________________________________________________________________")
                print("Ingresó un dato que no corresponde con lo pedido, intentelo de nuevo ") 
                print("______________________________________________________________________")
        
        while True:
            try: 
                if edad > 18 and residente:
                    print("Escoge la categoria! ")
                    print("1. Atletismo")
                    print("2. Ciclismo")
                    print("3. Patinaje")
                    print("4. Menu Principal")
                    opcion = int(input(f"Ingrese el numero para la carrera en la que {nombre} participara:  "))
                    if opcion == 1:
                        carrera = "atletismo"
                        break
                    elif opcion == 2:
                        carrera = "ciclismo"
                        break
                    elif opcion == 3:
                        carrera = "patinaje"
                        break
                    elif opcion == 4:
                        menu()
                        break   
                    else:
                        print("Error! ingrese un numero valido")

                elif edad > 18 and residente== False:
                    print("______________________________________________________________________")
                    print("El participante no pudo registrarse porque no es residente en Santander ")
                    break

            except ValueError:
                print("______________________________________________________________________")
                print("Ingresó un dato que no corresponde con lo pedido, intentelo de nuevo ") 
                print("______________________________________________________________________")
        if edad > 18 and residente:

            #participantes.append({"documetno": documento, "nombre": nombre, "edad": edad,"carrera": carrera,"residente": residente,"calificacion": 0})

            participantes[documento]={"nombre": nombre,
                                "edad": edad,
                                "carrera": carrera,
                                "residente": residente,
                                "calificacion": 0.0}
        else: 
            break
        participantesBD.guardar(participantes, "participantes.txt")
        #participantes=BD.cargar(participantes, "participantes.txt")
    print(participantes)
    return participantes

def calificaciones():
    participantes = participantesBD.cargar( "participantes.txt")
    if len(participantes)>0:
        while True:
                try:  
                    calificacion = 0   
                    for i in participantes:
                        if participantes[i]["calificacion"] == 0.0:
                            calificacion = float(input(f"Ingrese el tiempo de {participantes[i]['nombre']}: "))
                            participantes[i]["calificacion"] = calificacion
      
                    if calificacion > 1 or calificacion <=100:
                        print("El puntaje debe se entre 0 y 200")
                        break
                    elif participantes[i]["calificacion"] != "0":
                        print("No hay participantes sin calificar")
                        break
                    
                except ValueError:
                    print("______________________________________________________________________")
                    print("Ingreso un dato que no corresponde con lo pedido, intenelo de nuevo. ") 
    else:
        print("No hay participantes para la calificacion")
    participantesBD.guardar(participantes, "participantes.txt")

def listar_ranking():
    lista_ciclismo = []
    lista_atletismo = []
    lista_patinaje = []

    participantes = participantesBD.cargar("participantes.txt")
    contciclismo = 0
    contatletismo = 0
    contcpatinaje= 0
    for i in participantes.keys():
        #ciclismo+++++++++++++++++++++++++++++++++++++++
        if participantes[i]["calificacion"] != 0.0 and participantes[i]["carrera"] == "ciclismo":
            lista_ciclismo.append((participantes[i]["calificacion"],(participantes[i]["nombre"]) ))
        elif participantes[i]["calificacion"] == 0.0 and participantes[i]["carrera"] == "ciclismo":
            contciclismo += 1
            
        #atletismo+++++++++++++++++++++++++++++++++++++++
        if participantes[i]["calificacion"] != 0.0 and participantes[i]["carrera"] == "atletismo":
            lista_atletismo.append((participantes[i]["calificacion"],(participantes[i]["nombre"]) ))
        elif participantes[i]["calificacion"] == 0.0 and participantes[i]["carrera"] == "atletismo":
            contatletismo += 1
            
        #patinaje+++++++++++++++++++++++++++++++++++++++
        if participantes[i]["calificacion"] != 0.0 and participantes[i]["carrera"] == "patinaje":
            lista_patinaje.append((participantes[i]["calificacion"],(participantes[i]["nombre"]) ))
        elif participantes[i]["calificacion"] == 0.0 and participantes[i]["carrera"] == "patinaje":
            contcpatinaje += 1

    if contciclismo ==5:
        print("-----------------------------------")
        print("No hay tiempo registrados para el ranking de ciclismo")
    if  contatletismo ==5:
        print("-----------------------------------")
        print("No hay tiempo registrados para el ranking de atletismo")
    if contcpatinaje ==5:
        print("-----------------------------------")
        print("No hay tiempo registrados para el ranking de patinaje")
    
    
    lista_ciclismo_ordenada = sorted(lista_ciclismo, key=lambda tupla: tupla[0])
    lista_atletismo_ordenada = sorted( lista_atletismo, key=lambda tupla: tupla[0])
    lista_patinaje_ordenada = sorted( lista_patinaje, key=lambda tupla: tupla[0])

    if len(lista_atletismo) >= 5 :
        print("-----------------------------------")
        print("Primeros 5 puestos para atletismo")
        print("-----------------------------------")
        j = 0
        for i in lista_atletismo_ordenada[:5]:
            print(f"Puesto: {j+1}  Tiempo: {i[0]}, Nombre: {i[1]}")
            j += 1
    else:
        print("-----------------------------------")
        print("No hay participantes de atletismo para el ranking")

    if len(lista_ciclismo) >= 5:
        print("-----------------------------------")
        print("Primeros 5 puestos para ciclismo")
        print("-----------------------------------")
        j = 0
        for i in lista_ciclismo_ordenada[:5]:
            print(f"Puesto: {j+1}  Tiempo: {i[0]}, Nombre: {i[1]}")
            j += 1
    else:
        print("-----------------------------------")
        print("No hay participantes de ciclismo para el ranking")

    if len(lista_patinaje) >= 5:
        print("-----------------------------------")
        print("Primeros 5 puestos para patinaje")
        print("-----------------------------------")
        j = 0
        for i in lista_patinaje_ordenada[:5]:
            print(f"Puesto: {j+1}  Tiempo: {i[0]}, Nombre: {i[1]}")
            j += 1
    else:
        print("-----------------------------------")
        print("No hay participantes de patinaje para el ranking")
def menu():

    while True:
        print("""\n
        Menu Principal  
    1. Registrar participantes 
    2. Marcar ranking por carreras
    3. Listar ranking por carreras
    4. Salir\n""")
        
        opcion = int(input("Ingrese la opcion deseada: "))

        if opcion == 1:
            registrar_participantes()     
        elif opcion == 2:
            calificaciones()
        elif opcion == 3:
            listar_ranking()
        elif opcion == 4:
            validacions.confirmacion()
            print("Saliendo....")
            break
        else:
            print("Oopcion invalida ")