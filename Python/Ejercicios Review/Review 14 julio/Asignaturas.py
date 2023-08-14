asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
notas = list()

for i in asignaturas:
    nota = int(input(f"Ingrese la nota de {i}: "))
    notas.append(nota) 
    
print("+++++++++++++++++++++++++++++++")

for i in range(4):
    print(f"La nota de {asignaturas[i]} es: {notas[i]}")
    