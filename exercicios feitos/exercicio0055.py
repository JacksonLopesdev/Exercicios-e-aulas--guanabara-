n = int(input('digite um numero inteiro e eu lhe direi se ele e primo ou nao: '))
tot = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1 # aqui criada uma lista para ver quantas vezes o 'n' foi divisivel 
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(n, tot))
if tot == 2:
    print('o numero {} e divisivel somente por 1 e por ele mesmo, sendo assim numero primo.'.format(n))
else:
    print('o numero {} foi divisivel {} vezes, sendo assim nao e numero primo'.format(n, tot))
