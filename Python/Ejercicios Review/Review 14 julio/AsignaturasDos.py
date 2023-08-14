asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje"]
notas = list()

for i in asignaturas:
    nota = int(input(f"Ingrese la nota de {i}: "))
    notas.append(nota) 




print("+++++++++++++++++++++++++++++++")
print(asignaturas)
print(notas)
print("+++++++++++++++++++++++++++++++")

for nota,asi in zip(notas,asignaturas):
    
    if nota<=30:
        notas.remove(nota)
        asignaturas.remove(asi)
        print(f"La asignatura que debe aproabar es: {asi}")
    

  