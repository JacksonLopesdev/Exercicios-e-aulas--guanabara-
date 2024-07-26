aproveitamento = []
partidas_jogadas = 0

while True:
    nome = input('Nome do jogador: ')
    partidas_jogadas = int(input(f'Quantas partidas {nome} jogou? '))
    quantidade_de_gols = []
    for partida in range(partidas_jogadas):
        qtdde_de_gols = int(input(f'Quantidade de gols da partida {partida + 1}: '))
        quantidade_de_gols.append(qtdde_de_gols)
    
    total_gols = sum(quantidade_de_gols)
    jogador = {
        'nome': nome,
        'partidas jogadas': partidas_jogadas,
        'gols por partida': quantidade_de_gols,
        'total de gols': total_gols
    }
    aproveitamento.append(jogador)

    continuar = input('Quer continuar? [s/n]: ')
    if continuar.lower() != 's':
        break

print('='*80)
for jogador in aproveitamento:
    print(jogador)
    print('='*80)

for jogador in aproveitamento:
    print(f"O jogador {jogador['nome']} jogou {jogador['partidas jogadas']} partidas!")
    for partida, gols in enumerate(jogador['gols por partida']):
        print(f'Na partida {partida + 1}, marcou {gols} gols!')
