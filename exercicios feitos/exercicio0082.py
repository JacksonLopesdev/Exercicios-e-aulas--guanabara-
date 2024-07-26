pessoas = []
dados = []
contador = 0
while True:
    dados.append(str(input('nome: ')))
    dados.append(int(input('peso: ')))
    continuar = str(input('Quer continuar ? [S/N] '))
    pessoas.append(dados[:])
    dados.clear()
    contador += 1
    if continuar == 's':
        continue
    elif continuar == 'n':
        break
print(f'foram cadastradas {contador} pessoas.')
print(f'{pessoas}')
for p in pessoas:
    if p[1] >= 90:
        print(f'{p[0]} esta acima do peso com {p[1]} kilos !')
    elif p[1] <= 70:
        print(f'{p[0]} esta abaixo do peso com {p[1]} kilos !')

