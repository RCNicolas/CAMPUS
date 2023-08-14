import validations
import carsDB
from datetime import datetime
#registro = {"78787":{"entrada": 0,
            # "visitas": 0, "salida": 0, "valorpagado": 44545, "cobro": True}}

def parqueo():
    registro = carsDB.cargar_car("cars.json")
    if len(registro) != 0:
        cont = 0
        carrros = ""
        for i in registro.keys():
            if registro[i]["entrada"] == True:
                cont += 1
                carrros += i+"\n"
        if cont != 0:    
            print("-------------------------")            
            print("Carros en parqueadero: ")
            print("")
            print(carrros)
        else:
            print("NO hay carros en el parqueadero. ")
    else:
        print("-------------------------------")
        print("No se han registrado caros. ")

def recaudo():
    registro = carsDB.cargar_car("cars.json")
    pago = 0
    if len(registro) != 0:
        print("--------------------------------------------------------------")
        for info_carro in registro.values():
            for visita in info_carro["visitas"]:
                pago += visita["valor pagado"]
        print(f"valor recaudado: {pago}")
        print("--------------------------------------------------------------")
    else:
        print("-------------------------------")
        print("No se han registrado caros. ")

def historial():
    registro = carsDB.cargar_car("cars.json")
    if len(registro) != 0:
        print("---------------------------------------------------------------")
        for carro, info_carro in registro.items():
            print(f"Carro de placas: {carro}")
            print("")
            for visita in info_carro["visitas"]:
                ingreso= visita["hora ingreso"]
                salida= visita["hora salida"]
                pago= visita["valor pagado"]
                print(f"Hora ingreso: {ingreso}, hora salida: {salida}, valor pagado: {pago}")
            print("--------------------------------------------------------------")
    else:
        print("No se hay historial de carros. ")

def exit():

    registro = carsDB.cargar_car("cars.json")
    tarifa = carsDB.leer_tarifa("tarifa.csv")
    if len(registro) != 0:
        placa = validations.validate_variable_type("Ingrese la placa del carro.\n> ", "strcomple").upper()
        if placa in registro and not registro[placa]["cobro"]:
            
            registro[placa]["visitas"][-1]["hora salida"] = datetime.now().strftime('%d/%m/%y %H:%M')
            tiempo_parqueo = datetime.strptime(registro[placa]["visitas"][-1]['hora salida'], '%d/%m/%y %H:%M') - datetime.strptime(registro[placa]["visitas"][-1]['hora ingreso'], '%d/%m/%y %H:%M')
            tiempo_horas = tiempo_parqueo.total_seconds() / 3600
            valro_a_pagar = round(tiempo_horas * tarifa, 2)
            registro[placa]["visitas"][-1]['valor pagado'] = valro_a_pagar
            registro[placa]["cobro"] = True
            registro[placa]["salida"] = True
            registro[placa]["entrada"] = False
        else:
            print(f"El carro de placa {placa} no esta en el parqueadero. ")
    else:
        print("No hay vehiculos en el parqueadero. ")
    carsDB.guardar_car("cars.json", registro)

#  if visita['placa'] == placa and not visita['pagado']:
#             visita['salida'] = datetime.now().strftime('%d/%m/%y %H:%M')
#             tiempo_parqueo = datetime.strptime(visita['salida'], '%Y-%m-%d %H:%M:%S') - datetime.strptime(visita['entrada'], '%Y-%m-%d %H:%M:%S')
#             tiempo_horas = tiempo_parqueo.total_seconds() / 3600
#             tarifa = leer_tarifa('tarifa.txt')  # Cambiar por el nombre del archivo de tarifa
#             valor_a_pagar = round(tiempo_horas * tarifa, 2)
#             visita['valor_pagado'] = valor_a_pagar
#             visita['pagado'] = True

lista = []
def register():
    registro = carsDB.cargar_car("cars.json")
    
    placa = validations.validate_variable_type("Ingrese la placa del carro.\n> ", "strcomple").upper()
    
    if placa not in registro:
        
        registro[placa] = {"entrada": True,
                           "salida": False,
                           "cobro": False}
        lista=[{"hora ingreso": datetime.now().strftime('%d/%m/%y %H:%M'), "hora salida": 0,"valor pagado": 0}]
        registro[placa]["visitas"] = lista
        print("--------------------------------------")
        print(f"Placa {placa} registrada con exito. ")

    elif placa in registro and registro[placa]["entrada"] == False:
        lista = registro[placa]["visitas"]
        print(lista)
        lista.append({"hora ingreso": datetime.now().strftime('%d/%m/%y %H:%M'), "hora salida": 0,"valor pagado": 0})
        registro[placa] = {"entrada": True,
                           "salida": False,
                           "visitas": lista,
                           "cobro": False}
        
    elif placa in registro and registro[placa]["entrada"] == True:
        print("------------------------------------------------------------------")
        print(f"El carro con placa {placa} ya esta ingresado en parqueadero. ")
    else:
        print("---------------------------------------")
        print(f"La placa {placa} ya fue registrada. ") 
    carsDB.guardar_car("cars.json", registro)

