v1 = int(input('digite um valor: '))
v2 = int(input('agora mais um: '))
n = int(input('agora digite o numero que corresponde a operacao que voce deseja que eu faca: \n1 para: soma\n2 para: multiplicacao\n3 para: maior\n4 para: novos numeros\n5 para: sair'))
soma = v1 + v2
multiplicacao = v1 * v2
maior = max(v1, v2)
while n == 4:
    v1 = int(input('digite um valor: '))
    v2 = int(input('agora mais um: '))
    n = int(input('agora digite o numero que corresponde a operacao que voce deseja que eu faca: \n1 para: soma\n2 para: multiplicacao\n3 para: maior\n4 para: novos numeros\n5 para: sair'))
if n == 1:
    print('A soma do primeiro numero com o segundo e de: {}.'.format(soma))
elif n == 2:
    print('Os valores multiplicados, sao iguais ao valor: {}.'.format(multiplicacao))
elif n == 3:
    print('O maior valor entre eles e de: {}.'.format(maior))
elif n == 5:
    print('Tenha um excelente dia !')
    