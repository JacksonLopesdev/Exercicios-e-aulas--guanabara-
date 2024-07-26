lista = []
numeros_digitados = 0

while True:
    numero = input('Digite um numero: ')
    parar = input('Quer continuar ? [s/n]: ')
    lista.append(int(numero))
    numeros_digitados += 1
    
    if parar == 's':
        continue
    else:
        break

lista.sort(reverse=True)

if 5 in lista:
    posicao = lista.index(5)
    print(f'O numero 5 aparace na posicao {posicao}')
else:
    print('O numero 5 nao aparece na lista')


print(f'A lista em ordem decrescente fica:{lista}.\nForam {numeros_digitados} numeros digitados.')
