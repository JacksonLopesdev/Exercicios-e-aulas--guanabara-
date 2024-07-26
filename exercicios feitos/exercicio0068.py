nome = []
preco = []

while True:
    n = input('Digite o nome do produto:')
    p = int(input('Digite o preco: '))
    quer_continuar = input('quer continuar (s/n): ')
    nome.append(n)
    preco.append(p)
    if quer_continuar == 's':
        continue
    else:
        break
total_gasto = sum(preco)
mais_barato = min(preco)
maior_mil = 0
indice_mais_barato = preco.index(mais_barato) 

for i, precos in enumerate(preco):
    if preco[i] >= 1000:
        maior_mil += 1

print('O total gasto foi de {}.\n{} produtos custam mais de mil reais.\n{} é o produto mais barato.'.format(total_gasto, maior_mil, nome[indice_mais_barato]))
