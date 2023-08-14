"""
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación
 comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
 pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla 
 con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada 
 por la puntuación del nivel.

Nivel                 Puntuación
Inaceptable             0.0
Aceptable               0.4
Meritorio               0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que 
recibirá el usuario."""

puntuacion = float(input("Ingrese la puntuacion del usuario "))
cantidadBaseDinero = 2400

if puntuacion == 0.0:
    print("El epleado tiene un nivel Inaceptable ")
    print("El recibira un sueldo de: ", cantidadBaseDinero)
elif puntuacion == 0.4:
    cantidadBaseDinero += cantidadBaseDinero * puntuacion 
    print("El epleado tiene un nivel Aceptable ")
    print("El recibira un sueldo de: ", cantidadBaseDinero)
elif puntuacion >= 0.6:
    cantidadBaseDinero += cantidadBaseDinero * puntuacion 
    print("El epleado tiene un nivel Meritorio")
    print("El recibira un sueldo de: ", cantidadBaseDinero)
else:
    print("La puntuacion ingresada no es valida")