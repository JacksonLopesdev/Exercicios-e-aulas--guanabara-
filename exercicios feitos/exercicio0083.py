numeros = []
pares = []
impares = []
for n in range(7):
    entrada = int(input('digite um numero: '))

    if entrada % 2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)

pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
pares.clear()
impares.clear()
print(numeros)