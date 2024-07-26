import random

jkp = ['pedra', 'papel', 'tesoura']

while True:
    ppt = random.choice(jkp)
    eu = input('Pedra, papel, ou tesoura gafanhoto?: ').strip().lower()

    while eu not in jkp:
        print("Escolha inválida. Escolha entre 'pedra', 'papel' ou 'tesoura'.")
        eu = input('Pedra, papel, ou tesoura gafanhoto?: ').strip().lower()

    if eu == ppt:
        print('Empate! Vamos outra.')

    elif (eu == 'pedra' and ppt == 'tesoura') or (eu == 'tesoura' and ppt == 'papel') or (eu == 'papel' and ppt == 'pedra'):
        print('Parabéns, você ganhou!')
        break
    
    else:
        print('Você perdeu!')
        break
