""" Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus 
cuadrados"""

def funcion(muestra):
    lista = []
    for i in muestra:
        lista.append(i**2)
    return lista
muestra = [1, 2, 3, 4, 5]
print(muestra)
print(f"Lista de los cuadrados de los elementos: {funcion(muestra)}")