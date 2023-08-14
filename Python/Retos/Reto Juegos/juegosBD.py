import validaciones 

valoraciones ={}

# def cargar(file_name):
    
#     if validaciones.validate_file(file_name):       
#         with open(file_name,"w") as file:
#             for jue,valr in valoraciones.items():
#                 file.write(f"{jue}|")
#                 for ele in valr:
#                     file.write(f"{ele}-")
#                 file.write("\n")
        

# def guardar(file_name):
#     valoracion ={}
#     if validaciones.validate_file(file_name):            
#        with open(file_name,"r") as file:
#             lista = file.readlines()
#             for line in lista:
#                 line = line.split("|")
#                 juego = line[0]
#                 valors = line[1].split("-")
#                 for er in valors:
#                     if(er=='\n'):
#                         valors.remove(er)
#                 for valor in valors:
#                     if(valoracion.get(juego,True)==True):
#                         valoracion[juego]=[int(valor)]
#                     else:
#                         valoracion[juego].append(int(valor))
#     return valoracion

def cargar(file_name):

    if validaciones.validate_file(file_name):       
        archivo = open(file_name, "r")
        lista = archivo.readlines()    
        archivo.close()
        valoraciones = []
        for i in lista:
            valoracion = i.split("|")
            valoraciones[valoracion[0]]=[valoracion[1]]
        return valoraciones
    else:
        return []

def guardar(valoracion,file_name):
    if validaciones.validate_file(file_name):            
        archivo = open(file_name, "w")
        lista = []
        for i in valoracion:
            print(i)
            nombre = str(i[0])
            valor = str(i[1])
            linea =  nombre + "|"  + valor + "|" + "\n"
            lista.append(linea)
        for i in lista:
            archivo.write(i)
        archivo.close()

def cargar_juegos(file_name):
    
    if validaciones.validate_file(file_name):       
        archivo = open(file_name, "r")
        lista = archivo.readlines()    
        archivo.close()
        juegos = {}
        for i in lista:
            participante = i.split("|")
            juegos[participante[0]]={"tiempo": int(participante[1]), "jugadores": int(participante[2]), "existencia": str(participante[3])}
        return juegos
    else:
        return {}

def guardar_juegos(juegos,file_name):
    if validaciones.validate_file(file_name):            
        archivo = open(file_name, "w")
        lista = []
        for i in juegos:
            nombre = str(i)
            tiempo = str(juegos[i]["tiempo"])
            jugadores = str(juegos[i]["jugadores"])
            existencia = str(juegos[i]["existencia"])
            linea =  nombre + "|"  + tiempo + "|" + jugadores + "|" + existencia + "|" + "\n"
            lista.append(linea)
        for i in lista:
            archivo.write(i)
        archivo.close()