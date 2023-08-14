abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for posicion, valor in enumerate(abecedario):
    if posicion%3 ==0:
        print(posicion)
        abecedario.remove(valor)

print(posicion,abecedario)