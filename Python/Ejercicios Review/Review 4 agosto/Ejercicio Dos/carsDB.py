import json
import csv 

def leer_tarifa(file_name):
    
    with open(file_name,"r", newline="") as file:
        tarifa = float(file.read())
    return tarifa

def cargar_car(file_name):
    try:
        with open(file_name, "r") as file:
            data= json.load(file)
            return data
    except FileNotFoundError:
        return {}
    except Exception:
        return{}
    
def guardar_car(file_name, datos):
    try:
        with open(file_name, "w") as file:
            json.dump(datos, file)
            return True
    except FileNotFoundError:
        return False
    except Exception:
        return False