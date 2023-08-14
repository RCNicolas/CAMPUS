palabra = input("Ingrese una palabra: ")
cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

for i in palabra:
  if i ==  "a":
    cont_a += 1
  elif i == "e"  :
    cont_e += 1
  elif i == "i":
    cont_i += 1
  elif i == "o":
    cont_o += 1
  elif  i == "u":
    cont_u += 1
    
print(f"La cantidad de vocales a en la palabra es: {cont_a}")
print(f"La cantidad de vocales e en la palabra es: {cont_e}")
print(f"La cantidad de vocales i en la palabra es: {cont_i}")
print(f"La cantidad de vocales o en la palabra es: {cont_o}")
print(f"La cantidad de vocales u en la palabra es: {cont_u}")