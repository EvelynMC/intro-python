# Acá va un comentario  
if 3 > 5:
    print('Esto no se va a imprimir')
#if 5 > 3:
#    print('5 es mayor a 3')

x = 5
y = 'Chanchito Feliz'

# print(x,y)

correo = 'chanchito@feliz.com'

# print(correo)

mi_var = 'chanchito'

a, b, c = 'Lala', 'Lele', 'Lili'

# print (a, b, c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'

# print(valor1, valor2, valor3)

inicio = 'Hola'
final = 'mundo'

# print(inicio + final)  #concatenacion

# Tipos de datos básicos

palabra = 'hola mundo' #string
oracion = "hola mundo comilla simple" #string

entero = 20    #integer
decimal = 20.2   #float
complejo = 1j 

# print (palabra, oracion, entero, decimal, complejo)


# -- LISTAS: colección de datos -- 

lista = ['Hola', 'Mundo', 'Chanchito Feliz']
lista2 = lista.copy()
lista.append('Chanchito Triste')
#lista.clear()


# print(lista, lista2.count(3))
# print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)

# print(largoLista, largoLista2)

# print(lista[2])

# lista.pop()   #Este método elimina el ultimo elemento de la lista
# lista.remove('Hola') # Este elimina un elemento por su valor

lista.reverse()
lista.sort()  #no soporta mismos tipos de datos

# print(lista)

# -- TUPLAS: Una vez creadas NO PUEDEN MODIFICARSE

tupla = ('hola', 'mundo', 'somos', 'tupla')
listaDeTupla = list(tupla)  # transformar lista a tupla
listaDeTupla.append('chanchito')

# print(listaDeTupla)

# -- RANGOS  --> Sirve para trabajar con las iteraciones

rango = range(6)

# print(rango)


# -- DICCIONARIOS

diccionario = {
    "nombre": "Chanchito Feliz",
    "raza": "Persa",
    "edad": 5
}

# print(diccionario['nombre'])
# print(diccionario['raza'])
# print(diccionario.get('nombre'))
# diccionario['nombre'] = 'Fluffy'

# print(len(diccionario))

diccionario["ronronea"] = 'Si'
# print(diccionario)

# diccionario.pop('ronronea')    # elimina un valor del diccionario
# print(diccionario)

copiaGatito = diccionario.copy()
# del diccionario['ronronea']
diccionario.clear()      #elimina todos los valores de un diccionario
# diccionario.popitem() #elimina ultimo valor del diccionario
# print(diccionario, copiaGatito)

# DICCIONARIOS ANIDADOS

fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}

mamba = {
    "nombre":"Black Mamba",
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6)

print(perritos)

verdadero = True
falso = False

print(verdadero, falso)

