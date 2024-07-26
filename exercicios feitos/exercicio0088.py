from random import randint 
from time import sleep 

resultados = {}

for i in range(4):
    dado = randint(1, 6)  
    chave = f'O jogador {i} tirou' 
    resultados[chave] = dado
    resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

for chave, valor in resultados.items():
    sleep(0.5)  
    print(f'{chave}: {valor}')
print('Ranking dos jogadores:')
for i, (chave, valor) in enumerate(resultados_ordenados):
    sleep(0.5)
    print(f'{i+1}º lugar: {chave}: {valor}')
