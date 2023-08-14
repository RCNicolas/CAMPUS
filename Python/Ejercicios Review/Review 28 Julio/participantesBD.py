import validacions

# participantes[documento]={"nombre": nombre,
#                           "edad": edad,
#                           "carrera": carrera,
#                           "residente": residente,
#                           "calificacion": ""}
#participantes.append({"documetno": documento, "nombre": nombre, "edad": edad,"carrera": carrera,"residente": residente,"calificacion": 0})

def cargar(file_name):

    if validacions.validate_file(file_name):       
        archivo = open(file_name, "r")
        lista = archivo.readlines()    
        archivo.close()
        participantes = {}
        for i in lista:
            participante = i.split("|")
            residente = False
            if participante[4] == "True":
                residente = True
            participantes[participante[0]]={"nombre": participante[1], "edad": int(participante[2]), "carrera": str(participante[3]), "residente": residente, "calificacion": float(participante[5])}
        return participantes
    else:
        return {}

def guardar(users,file_name):
    if validacions.validate_file(file_name):            
        archivo = open(file_name, "w")
        lista = []
        for i in users:
            documento = str(i)
            nombre = str(users[i]["nombre"])
            edad = str(users[i]["edad"])
            carrera = str(users[i]["carrera"])
            residente = str(users[i]["residente"])
            calificacion = str(users[i]["calificacion"])
            linea = documento + "|" + nombre + "|" + edad + "|" + carrera + "|" + residente + "|" + calificacion + "|" + "\n"
            lista.append(linea)
        for i in lista:
            archivo.write(i)
        archivo.close()