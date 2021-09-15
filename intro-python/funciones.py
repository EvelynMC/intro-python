# Funciones:

def miFuncion():
    print("Mi primera función")

# miFuncion()

def imprimeDato(*nombre):    # Se pasa argumento a la función para utilizarse
    print('El nombre completo es', nombre)

# imprimeDato('Chanchito', 'Feliz', 'Lala', 'Lele')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

# nombreCompleto(nombre='Chanchito', apellido='Feliz')      # En caso de no recoradar el orden de los argumentos, se puede ingresar con la llave.


def nombreCompleto2(**kwargs):                   # Se aggrupan argumentos como diccionario
    print(kwargs['nombre'], kwargs['apellido'])

# nombreCompleto2(nombre='Chanchito', apellido = 'Feliz')


def miFuncion2(argumento = 'Chanchito'):    # Si no se pasa argumento, define uno por defecto
    print(argumento)

# miFuncion2('Batman')
# miFuncion2()


def miFuncionLista(lista):
    for el in lista:
        print(el)

# miFuncionLista(['Chanchiito', 'Feliz'])

def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

# nombres = concatenaNombres(['Chanchito', 'Feliz', 'Gato'])
# print(nombres)    


# Recursividad en funciones: Sirve para cuando se trabaja con datos o reconexión a base de datos, por ejemplo

def recursion(i):
    if(i < 1):
        return i 
    print(i)
    recursion(i - 1)

recursion(6)