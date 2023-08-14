import validations

def cargar(file_name):
    if validations.validate_file(file_name):       
        archivo = open(file_name, "r")
        lista = archivo.readlines()    
        archivo.close()
        events = []
        for i in lista:
            event = i.split("|")
            is_done = False
            if event[3] == "True":
                is_done = True
            events.append({'name': event[0], 'location': event[1], 'day': int(event[2]), 'is done': is_done})            
        return events
    else:
        return []

def guardar(events,file_name):
    if validations.validate_file(file_name):            
        archivo = open(file_name, "w")
        lista = []
        for i in events:
            name = i["name"]
            location = i["location"]
            day = str(i["day"])
            is_done = str(i["is done"])
            linea = name + "|" + location + "|" + day + "|" + is_done + "|" +"\n"
            lista.append(linea)
        for i in lista:
            archivo.write(i)
        archivo.close()