from random import shuffle
a1 = str(input('nome do primeiro aluno:'))
a2 = str(input('nome do segundo aluno:'))
a3 = str(input('nome do terceiro aluno:'))
a4 = str(input('nome do quarto aluno:'))
la = [a1,a2,a3,a4]
shuffle(la)
print('os alunos do primeiro ao quarto sao: {}'.format(la))
