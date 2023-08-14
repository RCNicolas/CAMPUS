import json

def cargar_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except Exception:
        return []
    
def guardar_data(file_name, datos):
    try:
        with open(file_name, "w") as file:
            json.dump(datos, file)
            return True
    except FileNotFoundError:
        return False
    except Exception:
        return False