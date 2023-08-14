"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el 
diccionario."""

dic = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

divisa = input("Ingrese su disiva: ")

if divisa in dic.values():
    print(divisa)
else: 
    print(f"La divisa ingresada {divisa} no fue entontrada en el arreglo")
