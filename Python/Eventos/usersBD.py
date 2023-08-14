import validations

def cargar(file_name):
    if validations.validate_file(file_name):       
        archivo = open(file_name, "r")
        lista = archivo.readlines()    
        archivo.close()
        participantes = {}
        for i in lista:
            participante = i.split("|")
            paid = False
            if participante[4] == "True":
                paid = True
            participantes[participante[0]] = {"name": participante[1], "age": int(participante[2]), "area": participante[3], "is paid": paid}
        return participantes
    else:
        return {}

def guardar(users,file_name):
    if validations.validate_file(file_name):            
        archivo = open(file_name, "w")
        lista = []
        for i in users.keys():
            document = i
            name = users[i]["name"]
            age = str(users[i]["age"])
            area = users[i]["area"]
            paid = str(users[i]["is paid"])
            linea = document + "|" + name + "|" + age + "|" + area + "|" + paid + "|" +"\n"
            lista.append(linea)
        for i in lista:
            archivo.write(i)
        archivo.close()