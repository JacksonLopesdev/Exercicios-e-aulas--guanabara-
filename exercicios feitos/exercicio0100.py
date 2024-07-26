def ficha(jogador='', gols=0):
    jogador = input('Digite o nome do jogador: ')
    if jogador == '':
        jogador = 'Desconhecido'  
    
    gols = input('Quantos gols no campeonato: ')
    if gols == '':
        gols = 0  
    else:
        gols = int(gols)  
    
    print(f'O jogador {jogador}, fez {gols} gols no campeonato!')

# Uso da função
ficha()  
