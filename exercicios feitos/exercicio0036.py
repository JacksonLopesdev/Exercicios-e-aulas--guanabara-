salario = float(input('digite seu salario atual que calcularei seu aumento: '))
if salario >= 1250.00:
    print('seu novo salario e de {}, meus parabens !!'.format(salario *10 / 100 + salario))
else:
    print('seu novo salario e de {}, meus parabens !!'.format(salario * 15 / 100 + salario))