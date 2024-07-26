nome = dict()
nome['Nome'] = str(input('digite o nome do aluno: '))
nome['Media'] = float(input('Media: '))
if nome['Media'] < 5:
    print(f'{nome['Nome']} teve media de {nome['Media']} e esta reprovado !')

else:
    print(f'{nome['Nome']} teve nota {nome['Media']} e esta aprovado !')