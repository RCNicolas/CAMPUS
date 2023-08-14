"""4. Escribir una función que reciba una muestra de números en una lista y devuelva su media."""

def funcion(muestra):
    media = sum(muestra)/len(muestra)
    return media
muestra = [1, 2, 3, 4, 5]
print(f"Media: {funcion(muestra)}")