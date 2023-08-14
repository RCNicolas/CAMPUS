"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir 
la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la 
función sin pasarle el porcentaje de IVA, deberá aplicar un 21%"""

def factura_iva(cantidad, iva = 21):
    total = int( cantidad + (cantidad * iva) / 100)
    print(f"El valor con el iva aplicado es: {total}")
cantidad = int(input("Ingrese la cantidad a la cuala se le va a aplcar el iva: "))
iva = int(input("Ingrese el iva que quiere aplicar: "))
factura_iva(cantidad, iva)