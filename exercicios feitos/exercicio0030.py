from random import randint
from time import sleep

palpites = []
np = randint(1,11)

resposta = int(input('vou pensar em um numero de 1 a 11, tente advinhar eu newbasso: '))

while resposta != np:
    print('processando ...')
    sleep(0.5)
    print('Tente de novo:')
    resposta = int(input('vou pensar em um numero de 1 a 11, tente advinhar eu newbasso: '))
if resposta == np:
    palpites.append(resposta)
print('parabens, voce acertou na mosca, seu numero de tentativas foi de : {}'.format(palpites))
    
    


