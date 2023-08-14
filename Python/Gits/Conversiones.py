# Conversión de entero a cadena (int to str)
#______________________________________________________________________________________________________________________________________
integer_value = 42
integer_to_string = str(integer_value)
print(f"int to str: {integer_to_string}, type: {type(integer_to_string)}")
# Salida: int to str: 42, type: <class 'str'>

# Conversión de cadena a entero (str to int)
#______________________________________________________________________________________________________________________________________
string_value = "123"
string_to_integer = int(string_value)
print(f"str to int: {string_to_integer}, type: {type(string_to_integer)}")
# Salida: str to int: 123, type: <class 'int'>

# Conversión de flotante a entero (float to int)
#______________________________________________________________________________________________________________________________________
float_value = 3.14
float_to_integer = int(float_value)
print(f"float to int: {float_to_integer}, type: {type(float_to_integer)}")
# Salida: float to int: 3, type: <class 'int'>

# Conversión de entero a flotante (int to float)
#______________________________________________________________________________________________________________________________________
integer_value = 42
integer_to_float = float(integer_value)
print(f"int to float: {integer_to_float}, type: {type(integer_to_float)}")
# Salida: int to float: 42.0, type: <class 'float'>

# Conversión de cadena a flotante (str to float)
#______________________________________________________________________________________________________________________________________
string_value = "3.14"
string_to_float = float(string_value)
print(f"str to float: {string_to_float}, type: {type(string_to_float)}")
# Salida: str to float: 3.14, type: <class 'float'>

# Conversión de lista a cadena (list to str)
#______________________________________________________________________________________________________________________________________
my_list = [1, 2, 3]
list_to_string = str(my_list)
print(f"list to str: {list_to_string}, type: {type(list_to_string)}")
# Salida: list to str: [1, 2, 3], type: <class 'str'>

# Conversión de lista a tupla (list to tuple)
#______________________________________________________________________________________________________________________________________
my_list = [1, 2, 3]
list_to_tuple = tuple(my_list)
print(f"list to tuple: {list_to_tuple}, type: {type(list_to_tuple)}")
# Salida: list to tuple: (1, 2, 3), type: <class 'tuple'>

# Conversión de tupla a lista (tuple to list)
#______________________________________________________________________________________________________________________________________
my_tuple = (1, 2, 3)
tuple_to_list = list(my_tuple)
print(f"tuple to list: {tuple_to_list}, type: {type(tuple_to_list)}")
# Salida: tuple to list: [1, 2, 3], type: <class 'list'>

# Conversión de lista de tuplas a diccionario (list of tuples to dictionary)
#______________________________________________________________________________________________________________________________________
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
list_of_tuples_to_dict = dict(list_of_tuples)
print(f"list of tuples to dict: {list_of_tuples_to_dict}, type: {type(list_of_tuples_to_dict)}")
# Salida: list of tuples to dict: {'a': 1, 'b': 2, 'c': 3}, type: <class 'dict'>

# Conversión de entero a booleano (int to bool)
#______________________________________________________________________________________________________________________________________
integer_value = 1
int_to_bool = bool(integer_value)
print(f"int to bool: {int_to_bool}, type: {type(int_to_bool)}")
# Salida: int to bool: True, type: <class 'bool'>

# Conversión de cadena a booleano (str to bool)
#______________________________________________________________________________________________________________________________________
string_value = "True"
str_to_bool = bool(string_value)
print(f"str to bool: {str_to_bool}, type: {type(str_to_bool)}")
# Salida: str to bool: True, type: <class 'bool'>  # Cualquier cadena no vacía se evalúa como True

# Conversión de flotante a booleano (float to bool)
#______________________________________________________________________________________________________________________________________
float_value = 0.0
float_to_bool = bool(float_value)
print(f"float to bool: {float_to_bool}, type: {type(float_to_bool)}")
# Salida: float to bool: False, type: <class 'bool'>  # Cero (0.0) se evalúa como False, cualquier otro número se evalúa como True

# Conversión de booleano a entero (bool to int)
#______________________________________________________________________________________________________________________________________
bool_value = True
bool_to_int = int(bool_value)
print(f"bool to int: {bool_to_int}, type: {type(bool_to_int)}")
# Salida: bool to int: 1, type: <class 'int'>  # True se representa como 1

# Conversión de booleano a cadena (bool to str)
#______________________________________________________________________________________________________________________________________
bool_value = False
bool_to_str = str(bool_value)
print(f"bool to str: {bool_to_str}, type: {type(bool_to_str)}")
# Salida: bool to str: False, type: <class 'str'>  # False se representa como 'False'