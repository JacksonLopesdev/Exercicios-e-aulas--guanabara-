from time import sleep
from random import randint

lista_jogo = []
jogos = int(input('Quantos palpites voce quer que eu de para voce jogar na mega ?'))

for _ in range(jogos):
    jogo = [randint(1,60) for _ in range(6)]
    jogo.sort()
    lista_jogo.append(jogo)

print("Aqui estão seus palpites para a Mega-Sena:")

for i, jogo in enumerate(lista_jogo, start=1):
    
    sleep(0.5)
    print(f"Jogo {i}: {jogo}")
