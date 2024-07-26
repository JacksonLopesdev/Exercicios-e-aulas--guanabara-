pesos = [] # definindo o pesos como lista

for _ in range(5):
    peso = float(input('digite o peso: '))
    pesos.append(peso)

menor_peso = min(pesos)
maior_peso = max(pesos)

print('O maior peso da lista foi: {}.\nO menor peso da lista foi: {}'.format(maior_peso, menor_peso)) #para poder printalo aqui
      