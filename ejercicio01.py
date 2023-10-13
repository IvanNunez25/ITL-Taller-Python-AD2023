''' Dada una lista imprimir números menores a 5 '''

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Ciclo for
for i in lista:
    if i < 5:
        print(i)

# list comprehension
print([x for x in lista if x < 5])