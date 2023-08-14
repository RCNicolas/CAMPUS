participantes = {}
def guardar(participantes):
    archivo = open("archivo.txt", "w")
    lista = []
    for i in participantes.keys():
        document = i
        name = participantes[i]["name"]
        age = str(participantes[i]["age"])
        area = participantes[i]["area"]
        paid = str(participantes[i]["is paid"])
        linea = document + "|" + name + "|" + age + "|" + area + "|" + paid + "|" +"\n"
        lista.append(linea)
    
    for i in lista:
        archivo.write(i)
    archivo.close()

def leer(participantes):
    archivo = open("archivo.txt", "r")
    lista = archivo.readlines()    
    archivo.close()
    participantes2 = {}
    for i in lista:
        participante = i.split("|")
        paid = False
        if participante[4] == "True":
            paid = True
        participantes2[participante[0]] = {"name": participante[1], "age": int(participante[2]), "area": participante[3], "is paid": paid}
    
    print(participantes2)
guardar(participantes)
leer(participantes)