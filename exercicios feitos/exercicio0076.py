lista = []

for n, item in enumerate(range(5)):
    lista.append(int(input('digite um numero: ')))

maior_numero = max(lista)
menor_numero = min(lista)
posicao_maior = lista.index(maior_numero)
posicao_menor = lista.index(menor_numero)

print(f'A lista e {lista}.\nO maior numero {maior_numero}, posicao {posicao_maior}.\nO menor numero {menor_numero}, posicao {posicao_menor}. ')