"""1. Una empresa requiere un sistema para controlar el ingreso de 
los empleados diariamente a la empresa. Para esto se requiere un menú 
con las siguientes funcionalidades:

Registrar empleado

Listar todos los empleados
Modificar empleados
Despedir empleados (Esta función no elimina al empleados solo cambia 
su estado)
Registrar entrada empleados
Registrar salida de empleados

Para que el aplicativo funcione correctamente se debe tener en cuenta:
Los empleados son registrados y manipulados en archivos de tipo json
la entrada es a las 8:00 am y la salida a las 6:00 pm por lo tanto a 
los empleados se les marca advertencia cuando llegan después de la 
hora o salen antes de la hora. 

Cada entrada y salida de empleados se debe registrar en un archivo 
txt o csv añadiendo línea a línea cada registro y no se debe 
modificar ni reescribir. Si el registro de entrada o salida aplica 
para alguna advertencia se debe marcar en el archivo también."""


import menus

menus.menu_principal()