lista = []

for _ in range(5):
    numero = int(input('digite um numero: '))
    lista.append(numero)

for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1
    while j >= 0 and chave < lista[j]:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = chave
    print(f'Lista atual: {lista}, Posição do número {chave}: {j + 1}')

print(f'A lista em ordem crescente é: {lista}')