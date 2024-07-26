from random import choice
a1 = input('digite o nome do aluno 1:')
a2 = input('digite o nome do aluno 2:')
a3 = input('digite o nome do aluno 3:')
a4 = input('digite o nome do aluno 4:')
a = [a1,a2,a3,a4]
g = choice(a)
print('nosso querido vencedor e: {}.'.format(g))