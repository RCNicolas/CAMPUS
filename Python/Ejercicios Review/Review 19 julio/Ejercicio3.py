"""3. Escribir una función que calcule el área de un cuadrado y otra que calcule el volumen de un cubo 
usando la primera función"""

def area_cuadrado(lado):
    area = lado**2
    return area

def area_cubo(lado):
    area = area_cuadrado(lado) * 6
    return area
lado = int(input("Ingrese la medida de un lado del cuadrado o un cubo: "))
 
print(f"El area del cuadrado es: {area_cuadrado(lado)}")
print(f"El area del cubo es: {area_cubo(lado)}")
