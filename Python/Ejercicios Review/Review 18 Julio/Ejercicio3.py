"""3. Escribir un programa que guarde en un diccionario los precios de las verduras de la tabla, pregunte al 
usuario por una verdura, un número de kilos y muestre por pantalla el precio a pagar. Si la fruta no está en 
el diccionario debe mostrar un mensaje informando de ello.

Verdura               Precio (Kg)
Brócoli                2500 COP
Pimentón               1250 COP
Arveja                 3500 COP"""

dic = {"verdura": ["Brócoli", "Pimentón", "Arveja" ],
       "precio": [2500, 1250, 3500]}

verdura = input("Que verdura desea comprar? ")
cantidad = int(input("Cuantos kg desea comprar? "))
precioFinal = 0
j = 0

if verdura in dic["verdura"]:
    for i in dic["verdura"]:
        if verdura == i:
            precioFinal = cantidad*dic["precio"][j]
            print(f"El precio por {cantidad}Kg de {verdura} es: {precioFinal}")    
        j += 1
else:
    print(f"No hay {verdura} disponible")

