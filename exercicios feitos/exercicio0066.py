from random import randint
ganhei = []
while True:
    jogada = int(input('Vamos jogar par ou impar ?\nEscolha um numero: '))
    computador = randint(1,100)
    if jogada % 2 == 0 and computador % 2 == 0:
        print('voce jogou par e eu tambem, assim ganhou')
        ganhei.append(1)
    elif jogada % 2 == 1 and computador % 2 == 1:
        print('voce jogou impar e eu tambem, assim ganhou')
        ganhei.append(1)
    else:
        print('Voce perdeu.')
        print('Voce ganhou {} vezes !!'.format(sum(ganhei)))
        break