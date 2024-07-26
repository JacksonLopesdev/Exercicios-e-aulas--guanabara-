nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('digite a segunda nota por favor: '))
media = (nota_1 + nota_2) / 2
if media < 5.0:
    print('Aluno reprovado !')
elif 5.0 <= media  < 7.0:
    print('O aluno esta de recuperacao !!')
else:
    (print('O aluno esta aprovado !!'))