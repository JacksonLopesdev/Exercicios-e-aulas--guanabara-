from math import factorial
n = int(input('digite um numero que lhe darei o resulado do fatorial do msm !: '))
f = factorial (n)
if n == 0:
    print('0 x 0 = ')
else:
    print('{} fatorial = {}.'.format(n, f))