#TIPOS DE EXCEPCIONES================================================
#___________________________________________________________________
#TypeError
#====================================================================
"""Ocurre cuando se aplica una operación o función a un 
dato del tipo inapropiado"""

#ZeroDivisionError
#====================================================================
"""Ocurre cuando se itenta dividir por cero"""

#OverflowError
#====================================================================
"""Ocurre cuando un cálculo excede el límite para un 
tipo de dato numérico."""

#IndexError
#====================================================================
"""Ocurre cuando se intenta acceder a una secuencia con 
un índice que no existe"""

#KeyError
#====================================================================
"""Ocurre cuando se intenta acceder a un diccionario con 
una clave que no existe."""

#FileNotFoundError
#====================================================================
"""Ocurre cuando se intenta acceder a un fichero 
que no existe en la ruta indicada."""

#ImportError
#====================================================================
"""Ocurre cuando falla la importación de un módulo."""

#Exception
#====================================================================
"""Para hacer uso general de las excepciones, las abarca todas pero 
no se puede usar para espeficicar el tipo de excepcion"""

def division (a,b):
    try:
        result = a/b
        print(result)
    except ZeroDivisionError:
        print("Error! No se puede dividir por cero. ")
    else: 
        print("Division realizada! ")