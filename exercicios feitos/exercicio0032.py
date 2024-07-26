n = int(input('digite um numero inteiro qualquer, que irei identificar se e par ou impar: '))
r = n % 2
if r == 0:
    print('seu numero e {}, par !!'.format(n))
else:
    print('seu numero e, {}, impar'.format(n))
