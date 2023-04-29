print("hola mundo")

# Variables y tipos datos

### Tipos de datos simples
enteros = 11 # int -> integer -> entero/// = es operador de asignacion
reales = 11.2 # float -> reales (?)

# tipos string, cadenas de caracteres
strings = 'hola'
strings1 = "hola"
strings3 = f"hola"
strings4 = '''hola''' # strings4[0] devuelve h

bool_verdadero = True
bool_falso = False

### Tipos de datos complejos
listas = [1, 3, 4, 5] # 
listas[0] # devuelve 1
listas[1] # devuelve 3
listas[2] # devuelve 4
listas[3] # devuelve 5

listas.sort() # ordeno la lista, tienen valores ordenables como por ejmplo, numeros
listas.reverse() # listas = [5, 4, 3, 1]

# agregar elementos
listas.append(32)

# sacar elementos
listas = [32, 13, 10, 54]
listas.pop() # elimino el ultimo elemento, elimino 54
listas.pop(1) # saca por indice, en este caso el num 13
# listas.remove(13) # saca por valor

# son estructuras de datos complejas estaticas
tuplas = (1, 3, 32, 13, 15)
print('elemento de la posicion 2:', tuplas[2])
# tuplas[2]=23 # no se puede cambiar los valores de las tuplas
# print(tuplas[2])

valores_tuplas = list(tuplas)
print(type(valores_tuplas)) # type() para saber el tipo de dato
print("antes de cambiar", valores_tuplas)
valores_tuplas[2]=23
print("despues de cambiar", valores_tuplas)

# Estudiarrrr --> dict, set
