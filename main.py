import random
regalos = ['Hojas', 'Almohadas', 'iPhone', 'Cocina', 'Puerta', 'Tablet', 'Llavero', 'Zapatos', 'Automovil', 'Bolso']

for serie in range(3):
    print('\n Serie: ', serie + 1)

print('\n')

random.seed(10)

for sorteo in range(len(regalos)):
    regalo = regalos[random.randint(0,9)]
    print('Sorteo', sorteo + 1, ':', regalo)
    #print('Sorteo', sorteo + 1, random.choice(regalos))