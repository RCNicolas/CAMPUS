participantes=[{"nombre": "Nicolas","edad": 20,"carrera": "cilismo","residente": True,"calificacion": 1.20},
               {"nombre": "Kevin",  "edad": 20,"carrera": "cilismo","residente": True,"calificacion": 1.40},
               {"nombre": "Pachon", "edad": 20,"carrera": "atletismo","residente": True,"calificacion": 6.20},
               {"nombre": "Marquez","edad": 20,"carrera": "atletismo","residente": True,"calificacion": 3.20}]

lista_cilismo = []
lista_atletismo = []
aux = 0
for i in range(len(participantes)):
    if participantes[i]["carrera"] == "cilismo":
        lista_cilismo.append((participantes[i]["calificacion"],(participantes[i]["nombre"]) ))
        print(lista_cilismo)
    if participantes[i]["carrera"] == "atletismo":
        lista_atletismo.append((participantes[i]["calificacion"],(participantes[i]["nombre"]) ))
        print()

lista_cilismo_ordenada = sorted(lista_cilismo, key=lambda tupla: tupla[0])
lista_atletismo_ordenada = sorted( lista_atletismo, key=lambda tupla: tupla[0])
print(lista_cilismo_ordenada)
print( lista_atletismo_ordenada)

for i in lista_atletismo_ordenada:
    print(f"Tiempo: {i[0]}, Nombre: {i[1]}")