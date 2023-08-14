"""2 .Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un 
diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su 
número de teléfono es <teléfono>."""

dic = {"nombre": 0, "edad": 0, "direccion": 0, "telefono": 0}

for i in dic.keys():
    dic[i] = input(f"Ingrese su {i}: ")

print(f"{dic['nombre']} tine {dic['edad']} años, vive en {dic['direccion']} y su numero de telefono es: {dic['telefono']}")