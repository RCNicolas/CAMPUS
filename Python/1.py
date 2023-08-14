x = 5
y = 0

try:
    div = x/y
    print(div)
except ZeroDivisionError:
    print("Erros division por cero ")
else: 
    print(f"Divisio realizada {div}")