print("Hello World")

# Operadores

print(5 == 2)
print(10 // 3) #Esto es una division floor

print("Hola" + " Python") #Concateno strings con esto. No puedo restar, solo el + es igual a contactenar
print("Hola"*2) #Se puede multiplicar un string

# Operadores de comparacion:

print(3 <= 4)

# Operadores lógicos

print(3 == 4 or "Hola" == "Hola")
print(4 in (3,2))
print(not(3 > 4)) # El not cambia el sentido de la condicion

## STRINGS

my_string = "Texto ejemplo"
my_other_string = 'Texto ejemplo2. Funcionan ambas comillas'

print(len(my_string)) # Con len() tengo la longitud
print(my_string + " "+ my_other_string) # Concatenacion de strings

my_new_string = "String con \nsalto de linea" #Salto de linea
print(my_new_string)

print("\t texto con tabulacion")

nombre = "Tomas"
apellido = "Roel"

print("Mi nombre es: %s %s" %(nombre, apellido)) # Asi funciona
print("Mi nombre es: %s %s".format(nombre, apellido)) # Este no funciona

# Para hacer el format lo hacemos asi:
print("Mi nombre es: {} {}".format(nombre, apellido))
print(f"Mi nombre es: {nombre} {apellido}")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b) # Lo que estamos haciendo es sacando los caracteres del string

# Division
language_slice = language[1:3]
print(language_slice) # Nos tomo la segunda (la primera es 0) y la segunda (sin la tercera)
print(language[1:])
print(language[-2]) # De atras para adelante, el segundo
# Revese
reversed_language = language[::-1] # De atras para adelante siempre se arranca por -1, no hay -0
print(reversed_language)

# Funciones
print(language.capitalize()) # Primera letra en mayuscula
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.upper().isupper())

