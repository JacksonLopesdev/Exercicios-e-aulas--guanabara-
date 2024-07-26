n1 = int(input('digite 1 numero qualquer (inteiro): '))
n2 = int(input('digite + 1 numero qualquer (inteiro): '))
if n1 > n2:
    print('{} e maior que {}.'.format(n1,n2))

elif n1 == n2:
    print('{} e {}, sao numeros iguais.'.format(n1, n2))

else:
    print('{} e menor que {}'.format(n1,n2))
    