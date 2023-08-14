"""
Una empresa está organizando la agenda de eventos para el mes de agosto. Por lo tanto requiere un programa que:

1. Permita registrar a los participantes de los eventos de agosto pidiendo: documento, nombre, edad y cargo.
2. Permita registrar los eventos  pidiendo: nombre del evento, locación y día del mes
3. Permita quitar del registro a los participantes.
4. Permita eliminar y/o modificar eventos.

Para participar los empleados deben cancelar un aporte de 50.000 COP. Por lo tanto el programa también debe:

    Saber cuantos empleados no han cancelado aún el aporte y cuanto dinero suma la deuda.
    Saber cuales empleados (listarlos) no han cancelado.
    No permitir quitar del registro a participantes que ya hayan pagado, pues no se aceptan devoluciones
    Marcar eventos ya realizados.
    No permitir eliminar o modificar eventos ya realizados.

Aspectos a tener en cuenta: 

La estructura a utilizar es libre, solo se pide que sea ordenada y coherente. 
Todo debe ser dentro de un menú que se repite para no perder la información y al presionar la opción de salida 
se debe pedir confirmación de la misma. 
Se deben manejar la excepciones"""

import module

participantes = {}
eventos = {}
confirmar = True
opcion = 1
while confirmar:

    opcion = module.menu()
    
    if opcion == 1:
        module.registrar_participantes(participantes)
    elif opcion == 2:
        module.registrar_eventos(eventos)
    elif opcion == 3:
        module.eliminar_prticipantes(participantes)
    elif opcion == 4:
        module.eliminar_modificar_eventos(eventos)
    elif opcion == 5:
        module.deuda(participantes)
    elif opcion == 6:
        module.modificar_participantes(participantes)
    elif opcion == 7:
        confirmar = input("Esta seguro de querer salir? se va a borrar todo\n(s/n) ").lower()
        if confirmar == "n":
            continue
        elif confirmar == "s":
            confirmar = False
        else: 
            print("Opcion invalida")
    else: 
        continue
        