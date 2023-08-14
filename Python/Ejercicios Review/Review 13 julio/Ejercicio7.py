numeros = list()
numeros = list(input("Ingrese una muestra de numeros separados por comas: "))
suma = 0
index = 0
for i in numeros:
  if i == ",":
    numeros.remove(",")
  else: 
    print(i)

for i in numeros:
  print(i)
  suma += int(i)
  

index = len(numeros)
promedio = suma/index
print(f"El promedio de los numeros ingresados es: {promedio}")

