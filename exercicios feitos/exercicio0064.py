from statistics import mean
numeros = []

while True:
    recebidos = int(input('digite um numero: '))
    numeros.append(recebidos)
    resposta = input('quer continuar ? (sim ou nao): ').strip().lower()

    if resposta == 'sim':
        continue
    else:
        menor_valor = min(numeros)
        maior_valor = max(numeros)
        media = mean(numeros)
        print('O maior numero entre eles foi {}, o menor {}, e a media e de {}.'.format(maior_valor, menor_valor, media))