''' Dada una entrada, imprimir los divisores de ese número '''

num = int(input("Introduce un número: "))

print([i for i in range(1, num) if num%i == 0])