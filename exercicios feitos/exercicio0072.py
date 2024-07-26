from random import randint

tupla = ()

for t in range(5):
    aleatorios = randint(1, 1000)
    tupla += (aleatorios, )

minimo = min(tupla)
maximo = max(tupla)

print(tupla)
print(maximo)
print(minimo)
