palabra = input("Ingrese una plabra ")
palabra = palabra.lower()

#inversa = palabra[::-1]
# if palabra == inversa:
#     print("Palindromo")

palabra = list(palabra)
inversa = palabra[::-1]

if palabra == inversa:
     print("Palindromo")