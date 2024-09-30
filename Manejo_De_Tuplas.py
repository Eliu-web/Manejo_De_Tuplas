# Imprime una línea en blanco
print(" ")

# Imprime el nombre del autor
print("Velazquez Mares Jesus Eliu")
print(" ")

# Crea una tupla con diferentes tipos de frutas
frutas = ("manzana", "platano", "melon", "sandia", "pera")
# Imprime la tupla de frutas
print(frutas)

# Crea una tupla con nombres, algunos nombres se repiten
nombres = ("juanito", "pepe", "pedro", "juanito", "pepe")
# Imprime la tupla de nombres
print(nombres)

# Crea una tupla con números
numeros = (1, 45, 75, 34, 34, 6, 356)
# Imprime la longitud de la tupla de números
print(len(numeros))

# Crea una tupla con un solo elemento (hola)
truetupla = ("hola",)
# Imprime el tipo de la tupla (debería ser <class 'tuple'>)
print(type(truetupla))

# Crea una variable que parece una tupla, pero no lo es (falta una coma)
falsetupla = ("hola")
# Imprime el tipo de la variable (debería ser <class 'str'>)
print(type(falsetupla))

# Crea una tupla con valores booleanos
tuple3 = (True, False, False)
# Imprime la tupla de booleanos
print(tuple3)

# Crea una tupla con diferentes tipos de datos
tipetuplas = ("qwer", 123, False, 463, "gey")
# Imprime la tupla con tipos variados
print(tipetuplas)

# Crea otra tupla de cadenas
tuplaaaaaaas = ("qwer", "asdf", "zxcv")
# Imprime el tipo de la tupla (debería ser <class 'tuple'>)
print(type(tuplaaaaaaas))

# Convierte una lista en una tupla y la imprime
thistuple = tuple(("apple", "banana", "cherry"))
# Imprime la tupla creada a partir de una lista
print(thistuple)