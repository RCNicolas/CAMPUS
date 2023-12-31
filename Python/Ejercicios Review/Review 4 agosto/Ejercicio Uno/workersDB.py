import json
import csv
def cargar(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        return {}
    except Exception:
        return {}
    
def guardar(file_name, datos):
    try:
        with open(file_name, "w") as file:
            json.dump( datos, file)
            return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
    
def guardar_registro(file_name,datos):
    try:
        with open(file_name, "a", newline="", encoding="UTF-8") as file:
            writer=csv.writer(file)
            writer.writerow(datos)
            return True
    except FileNotFoundError:
        return False
    except Exception:
        return False