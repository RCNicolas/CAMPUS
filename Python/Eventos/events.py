# eventos = [{"name": "paseo de rio", "location": "rio negro", "day": 15, "is done": False},
#            {"name": "paseo de rio", "location": "rio negro", "day": 15, "is done": False},
#            {"name": "paseo de rio", "location": "rio negro", "day": 15, "is done": False}
#         ]
import eventsBD

def create():
    
    events = eventsBD.cargar("EventosBD.txt")
    print("**********************************************************************")
    eve = {}
    name = input("Ingrese el nombre del evento: ")
    location = input("Ingrese la ubicación del evento: ")
    day = int(input("Ingrese el día del evento: "))
    eve = {"name": name, "location": location, "day": day, "is done": False}
    events.append(eve)
    print("Evento creado!!")
    print("**********************************************************************")
    eventsBD.guardar(events, "EventosBD.txt")

def update():
    
    events = eventsBD.cargar("EventosBD.txt")
    print("**********************************************************************")
    print("Ingrese el número del evento a modificar según la lista: ")
    for i in range(len(events)):
        print(i, "-", events[i])
    opc = int(input("Ingrese la opción deseada: "))
    if opc >= 0 and opc < len(events):
        if events[opc]["is done"]:
            print("Evento ya ejecutado!!")
        else:
            name = input("Ingrese el nombre del evento: ")
            location = input("Ingrese la ubicación del evento: ")
            day = int(input("Ingrese el día del evento: "))
            eve = {"name": name, "location": location, "day": day, "is done": False}
            events[opc] = eve
            print("Evento actualizado!!")
            print(events)
    else:
        print("Opción no valida")
    print("**********************************************************************")
    eventsBD.guardar(events, "EventosBD.txt")

def delete():
    events = eventsBD.cargar("EventosBD.txt")
    print("**********************************************************************")
    print("Ingrese el número del evento a eliminar según la lista: ")
    for i in range(len(events)):
        print(i, "-", events[i])
    opc = int(input("Ingrese la opción deseada: "))
    if opc >= 0 and opc < len(events):
        if events[opc]["is done"]:
            print("Evento ya ejecutado!!")
        else:
            events.pop(opc)
            print("Evento eliminado!!")
            print(events)
    else:
        print("Opción no valida")
    print("**********************************************************************")
    eventsBD.guardar(events, "EventosBD.txt")
def change_is_done():
    events = eventsBD.cargar("EventosBD.txt")
    print("**********************************************************************")
    print("Ingrese el número del evento a marcar como realizado: ")
    for i in range(len(events)):
        print(i, "-", events[i])
    opc = int(input("Ingrese la opción deseada: "))
    if opc >= 0 and opc < len(events):
        if events[opc]["is done"]:
            print("Evento ya ejecutado!!")
        else:
            events[opc]["is done"] = True
            print("Evento marcado como ejecutado!!")
            print(events)
    else:
        print("Opción no valida")
    print("**********************************************************************")
    eventsBD.guardar(events, "EventosBD.txt")