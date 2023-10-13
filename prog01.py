# Python es un lenguaje no tipado, osea que no requiere especificación de tipo de dato en las variables
x = 1.5
print(type(x))

# En Python no existen los arreglos, en su caso están las Listas
lista = [1, 2, 3, 4, 5]
print(len(lista))

# Tipos de datos
cadena = 'Hola'
entero = 13
decimal = 1.3
booleano = True
lista_ = [6, 7, 8, 9, 10]
it = iter(lista_)

lista.append("cadena")

print(type(lista_))

# Ciclos en Python
for i in lista:
    print(i)

lista.pop()
for i in lista:
    print(i)

while True:
    print(next(it))
    try:
        print(next(it))
    except StopIteration:
        break

# Listas -----------------------

lista.extend(lista_)
print(lista)

# Diccionarios (introducción)
# Un diccionario está compuesto por una llave y un valor -> { 'llave' : 'valor' }

diccionario = {
    'color': 'azul',
    'size': 'XL'
}

print(diccionario['color'])
print(diccionario['size'])

print(diccionario.keys())
print(diccionario.values())

it = iter(diccionario.keys())
it = iter(diccionario.values())

print(type(it))

diccionario['nombre'] = 'Ivan'

print('---------------- Diccionario -----------------')
for i in diccionario.keys():
    # Salidas formateadas: f'Texto normal {variable}'
    print(f'Llave: {i}, Valor: {diccionario[i]}')

# Tuplas. Las tuplas pueden contener diferentes valores en una misma variable
# A comparación de las listas, la tupla es inmutable

print('---------------- Tupla -----------------')

tupla = (10, 10, True, "x", 1.3)
print(tupla)
print(type(tupla))
print(iter(tupla))

# La propiedad index, regresa el valor del indice del primer valor encontrado
print(tupla.index(1.3))
print(tupla.index(10))

print(f'Total de 10 en la tupla: {tupla.count(10)}')

it = iter(tupla)
print(next(it))

print(' ---- Objetos en la tupla ----')
for i in tupla:
    print(i)

# Agregar la tupla a la Lista
# 'append' agrega toda la tupla en una sola posición de la Lista
# 'extend' agrega cada elemento de la tupla en su propia posición
lista_.append(tupla)
lista_.extend(tupla)
print(lista_)
