"""Escribe un programa que genere los primeros 4 números perfectos. Un número perfecto es un número entero 
positivo que es igual a la suma de sus divisores propios positivos. Dicho de otra forma, un número perfecto 
es aquel que es amigo de sí mismo. Así, 6 es un número perfecto porque sus divisores propios positivos son 
1, 2 y 3; y 6 = 1 + 2 + 3."""

numeros_perfectos = []
num = 1

while len(numeros_perfectos) < 4:
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    if num == suma:
        numeros_perfectos.append(num)
    num += 1

print("Los primeros 4 números perfectos son:")

print(numeros_perfectos)

