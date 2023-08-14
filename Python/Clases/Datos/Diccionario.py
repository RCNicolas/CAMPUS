dic ={
    "Nombre": "Nicolas",
    "Edad": 20,
    "Documento": 1234567890,
    "Es estudiante": True,
    "Mascota": {
        "Nombre": "michi",
        "Genero": "Macho",
        "Color": "azul",
        "Parents": {
            "madre": {
                "Edad": 5,
                "Nombre": "michita"
            },
            "padre": {
                "Edad": 5,
                "Nombre": "michito"
            }
        }
    },
    "Estudios": ["Bachiller", "Tecnico"],
    23: "Hola"
    
}
#acceder a un elemento
print(dic)
print(dic["Documento"])
print(dic[23])
print(dic.get("Nombre"))
print(dic["Estudios"][1])
print(dic["Mascota"]["Parents"]["padre"]["Edad"])

#operaciones que no modifican el dicionario
print(len(dic))#obtener tamaño del dic
#print(min(dic))#obtiene la llave de peso menor y cuando sean comparables
#print(max(dic))#obtiene la llave de peso mayor y cuando sean comparables
print("Edad" in dic)#saber si un llave esta en el diccionario
print(dic.keys())#obtener las llaves de un diccionario
print(dic.values())#obtener los valores de as llaves de un diccionario
print(dic.items())#obtener los elementos de un diccionario

#Recorrer diccionario 
for i in dic.keys():
    print(i, "->", dic[i])

for i in dic.items():
    print(i, "->")    

#operaciones que si modifican el diccionario
dic["Direccion"] = "Cra 12 #23-5"#añador elementos al diccionario
print(dic)
dic["Edad"] = 21#modificar elementos del diccionario
print(dic)
dic.pop("Mascota")#Eliminar el elemento del diccionario
print(dic)
Variable = dic.pop("Nombre", "adss")#Elimina el elemento del diccionario y lo devuelve, si la ñllave no existe marca error pero recibe un segundo parametro para devolver 
print(Variable)
del dic["Direccion"]#Eliminar el elemento con la ñllave pero si la llave no existe genera erros a diferencia del pop
print(dic)
dic.clear()#Elimina todos los elementos
print(dic)

dic1 = {"nombre": "Andres", "edad": 30}
dic2 = dict(dic1)#Copiando el diccionario por valores y asignandolo y no haciendo un apuntamiento a memoria
dic2["direccion"] = "aasdfgh"
print(dic1)
print(dic2)
