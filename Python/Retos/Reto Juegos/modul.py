import validaciones
import juegosBD

def top_valoraciones():
    valoraciones = juegosBD.cargar("datos_juegos.txt")
    juego = {}
    if not valoraciones:
        print("No hay valoraciones disponibles.")
        return
    for valoracion in valoraciones:
        for nombre, valoracion in valoracion.items():
            if not nombre in juego:
                juego[nombre] = 1
            else: 
                juego[nombre] = + 1

    for i in range(3):
        mayor = 0
        juego = ""
        for nombre, calificaciones in juego.items():
            if calificaciones > mayor:
                mayor = calificaciones
                juego = nombre
            if juego != "" and mayor != 0:
                print(f"{i+1}, {juego}: calificaciones: {mayor} ")
                juego.pop(juego)
    # for i in valoraciones:
    #     dic[valoraciones[0]]=valoraciones[1]
    #     print(dic)
    # sorted_valoraciones = dict(sorted(valoraciones.items(), key=operator.itemgetter(1), reverse=True))
    # top_tres = list(sorted_valoraciones.items())[:3]
    # for i, (juego, valoracion) in enumerate(top_tres):
    #     print(f"{i + 1}. Juego: {juego}, Valoración: {valoracion}")
    # valoraciones = leer_valoraciones()
    # if not valoraciones:
    #     print("No hay valoraciones disponibles.")
    #     return

    # sorted_valoraciones = dict(sorted(valoraciones.items(), key=operator.itemgetter(1), reverse=True))
    # top_tres = list(sorted_valoraciones.items())[:3]

    # print("\nTop tres juegos con más valoraciones:")
    # for i, (juego, valoracion) in enumerate(top_tres):
    #     print(f"{i + 1}. Juego: {juego}, Valoración: {valoracion}")
 

def valoracion():
    valoraciones = juegosBD.cargar("datos_juegos.txt")
    juegos = juegosBD.cargar_juegos("juegosBD.txt")
    if len(juegos) >0:
        print("Juegos disponibles ")
        for i in juegos.keys():
            print(i)
        
        try:
            nombre = input("Ingrese el nombre del juego que desea valorar: ")
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
        if nombre in juegos:
            while True:
                try:
                    valoracion = int(input(f"ingrese la valoración (entre 0 y 5) que le desea dar a {nombre}: "))
                    if valoracion <= 5 and valoracion >= 0:
                        valoraciones.append([nombre, valoracion])
                        break
                    elif valoracion > 5:
                        print("Valoracion fuera del rango")
                    elif valoracion < 0:
                        print("Valoracion fuera del rango")
                except ValueError:
                    print("---------------------------------")
                    print("Ingresaste un dato invalido")            
            else:
                print(f"El juego {nombre} no esta disponible ")
    else:
        print("No hay juegos registrados ")
    juegosBD.guardar(valoraciones, "datos_juegos.txt")
    juegosBD.guardar_juegos(juegos, "juegosBD.txt")

def registar():
    juegos = juegosBD.cargar_juegos("juegosBD.txt")
    while True:
        try:
            nombreJuego = input("Ingrese el nombre del juego ").lower()
            break
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
    while True:
        try:
            tiempo = int(input("Ingrese el tiempo en minutos por partida del juego "))
            break
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
    while True:
        try:
            cantidad_jugadores = int(input("Ingrese la cantidad de jugadores para el juego "))
            break
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
    while True:
        try:
            cantidad_disponible = int(input(f"Ingrese el numero de juegos disponibles de {nombreJuego} "))
            break
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
    juegos[nombreJuego] ={"tiempo": tiempo,
                          "jugadores": cantidad_jugadores,
                          "existencia": cantidad_disponible}
    juegosBD.guardar_juegos(juegos, "juegosBD.txt")
    
def modificar():
    juegos = juegosBD.cargar_juegos("juegosBD.txt")
    print("Juegos disponibles ")
    for i in juegos.keys():
        print(i)
    while True:
        try:
            nombre = input("Ingrese el nombre del juego que desea modificar ").lower()
            break
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
    if nombre in juegos:
        print("---------------------------------")
        print("1. Modificar tiempo por partida")
        print("2. Modificar cantidad de jugadores")
        print("3. Modificar existencia del juego")
        print("4. Menu pricipal ")
        print("---------------------------------")
        opcion = int(input("Ingrese la opcion deseada: "))

        if opcion == 1:
            while True:
                try:
                    tiempo = int(input("Ingrese el nuevo tiempo para el juego: "))
                    juegos[nombre]["tiempo"] = tiempo
                    break
                except ValueError:
                    print("---------------------------------")
                    print("Ingresaste un dato invalido")
        elif opcion == 2:
            while True:
                try:
                    cantidad = int(input(f"Ingrese la cantidad de jugadores para el juego de {nombre}: "))
                    juegos[nombre]["jugadores"] = cantidad
                    break
                except ValueError:
                    print("---------------------------------")
                    print("Ingresaste un dato invalido")
        elif opcion == 3:
            while True:
                try:
                    existencia = int(input(f"Ingrese la cantidad de juegos disponibles de {nombre}"))
                    juegos[nombre]["existencia"] = existencia
                    break
                except ValueError:
                    print("---------------------------------")
                    print("Ingresaste un dato invalido")
        elif opcion == 4:
            menu()
        else:
            print("Opcion invalida")
    else: 
        print("----------------------------------------")    
        print(f"El juego {nombre} no esta registrado \n")
    juegosBD.guardar_juegos(juegos, "juegosBD.txt")

def eliminar():
    juegos = juegosBD.cargar_juegos("juegosBD.txt")
    print("Juegos disponibles ")
    for i in juegos.keys():
        print(i)
    while True:
        try:
            nombre = input("Ingrese el nombre del juego que desea modificar ")
            break
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
    if nombre in juegos:
        print(f"El juego {nombre} fue eliminado exitosamente ")
        del juegos[nombre]
    else:
        print("----------------------------------------")    
        print(f"El juego {nombre} no esta registrado \n")
    juegosBD.guardar_juegos(juegos, "juegosBD.txt")

def consultar_juego():
    juegos = juegosBD.cargar_juegos("juegosBD.txt")
    if len(juegos.keys()) != 0:
        while True:
            try:
                tiempo = int(input("Ingrese su tiempo disponible (en minutos) para jugar "))
                break
            except ValueError:
                print("---------------------------------")
                print("Ingresaste un dato invalido")
        
        for i in juegos.keys():
            if juegos[i]["tiempo"] <= tiempo:
                print(f"Puede jugar {i} en base a su tiempo libre ")
            else: 
                print("No hay juegos disponibles para su tiempo ")
    else:
        print("No hay juegos disponibles")
    juegosBD.guardar_juegos(juegos, "juegosBD.txt")

def sub_menu_juegos():
    #juegos = juegosBD.cargar_juegos("juegosBD.txt")
    while True:
        try: 
            opcion = 0
            print("-------------------------")
            print("         Sub Menu        ")
            print("-------------------------")
            print("1. Registrar juego       ")
            print("2. Modificar juego       ")
            print("3. Eliminar juego        ")
            print("4. Menu principal        ")
            print("-------------------------\n")
            opcion = int(input("Ingrese la opcion deseada: "))
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
        except Exception:
            print("---------------------------------")
            print("Ingresaste un dato invalido")

        if opcion == 1:
            registar()
        elif opcion == 2:
            modificar()
        elif opcion == 3:
            eliminar()
        elif opcion == 4:
            
            break
        else:
            print("Opcion invalida")
        #juegosBD.guardar_juegos(juegos, "juegosBD.txt")    
        
def sub_menu_consultas():
    while True:
        try:
            print("-------------------------")
            print("         Sub Menu        ")
            print("-------------------------")
            print("1. Juegos para jugar     ")
            print("2. Valorar juego         ")
            print("3. Revisar puntuaciones  ")
            print("4. Menu principal        ")
            print("-------------------------\n")
         
            opcion = int(input("Ingrese la opcion deseada: "))
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
        except Exception: 
            print("---------------------------------")
            print("Ingresaste un dato invalido")

        if opcion == 1:
            consultar_juego()
        elif opcion == 2:
            valoracion()
        elif opcion == 3:
            top_valoraciones()
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")

def menu():
    while True:
        try:
            opcion = 0
            print("--------------------------")
            print("  MENÚ JUEGOS DE MESA     ")
            print("--------------------------")
            print("1. Gestion de juegos      ")
            print("2. Consultas y valoracion ")
            print("3. Salir                  ")
            print("--------------------------\n")
             
            opcion = int(input("Ingrese la opcion deseada: "))
        except ValueError:
            print("---------------------------------")
            print("Ingresaste un dato invalido")
        except Exception:
            print("---------------------------------")
            print("Ingresaste un dato invalido")

        if opcion == 1:
            sub_menu_juegos()
        elif opcion == 2:
            sub_menu_consultas()
        elif opcion == 3:
            validaciones.confirmacion()
            print("saliendo...")
            break
        else:
            print("Opcion invalida")
        
