"""2. Se necesita un aplicativo para controlar y cobrar la 
tarifa de un parqueadero. Para esto se requiere un menú con las 
siguientes funcionalidades:

> Registrar entrada con placa (Valor único e identificador)
> Marcar salida para cobrar
> consultar histórico de carros parqueados con hora salida y hora 
entrada de cada una de las visitas de cada carro y los valores 
cobrados.
> Consultar cantidades de dinero recaudado.
> saber cuales carros se encuentran parqueados en el momento.

Para que el aplicativo funcione correctamente se debe tener en 
cuenta:

> El valor de la tarifa por hora o fracción se debe registrar y 
leer desde un archivo txt o csv.
> El registro de carros, visitas se debe realizar en un archivo 
tipo json. Para cada carro se deben almacenar todas las visitas 
que haya hecho con entrada, salida y valor pagado. Además, se 
debe tener un atributo dedicado a saber si el valor fue pagado o 
no."""
import menus

menus.menu_principal()