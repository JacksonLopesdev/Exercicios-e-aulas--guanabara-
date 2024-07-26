dados = {}
idades = []
pessoas_cadastradas = 0
mulheres = []
acima_da_media = []

while True:
    nome = input('Nome: ')
    sexo = input('Sexo [m/f]: ').strip().lower()
    if sexo == 'f':
        mulheres.append(nome)
    idade = int(input('Idade: '))
    idades.append(idade)
    pessoas_cadastradas += 1
    media = sum(idades) / pessoas_cadastradas
    if idade > media:
        acima_da_media.append(nome)
    continuar = input('Quer continuar [s/n]: ').strip().lower()
    if continuar != 's':
        break

dados['nome'] = nome
dados['sexo'] = sexo
dados['idade'] = idade

print('=-' * 40)
print(f'O grupo tem {pessoas_cadastradas} pessoas.')
print(f'A média de idade é de {media}')
print(f'As mulheres cadastradas foram {mulheres}')
print('Lista de pessoas que estão acima da média da idade:')
print(acima_da_media)
