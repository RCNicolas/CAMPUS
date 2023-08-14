palabra = input("Ingrese una palabra: ")

for i in str(palabra[::-1]):
    if palabra == palabra[::-1]:
        palindromo = True
    else:
      palindromo = False
if palindromo == True:
  print(f"La palabra {palabra} es palindromo")        
else:
  print(f"La palabra {palabra} no es palindromo")        