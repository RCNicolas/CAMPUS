print("""
Binevenido a Bella Napoli
---------------------------""")

pizza = input("""
Que pizza desea?
-Vegetariana
-No vegetariana\n""")

if pizza == "Vegetariana":
    ingrediente = input("""
    Elige uno de los siguientes ingresientes
    -Pimenton
    -Tofu """)
    if ingrediente == "Pimenton":
        print("""Has elegido una pizza vegetariana con: \nPimenton \nMozarrella \nTomate """)
    elif ingrediente == "Tofu":
        print("Has elegido una pizza vegetariana con: \nTofu \nMozarrella \nTomate ")
    else:
        print("Has escogido una opcion incorrecta")
elif pizza =="No vegetariana":
    ingrediente = input("""
    Elige uno de los siguientes ingresientes
    -Pepperoni
    -Jamon
    -salmon """)
    if ingrediente == "Pepperoni":
        print("Has elegido una pizza no vegetariana con: \nPepperoni \nMozarrella \nTomate ")
    elif ingrediente == "Jamon":
        print("Has elegido una pizza no vegetariana con: \nJamon \nMozarrella \nTomate ")
    elif ingrediente == "salmon":
        print("Has elegido una pizza no vegetariana con: \nsalmon \nMozarrella \nTomate ")
else:
        print("Has escogido una opcion incorrecta")