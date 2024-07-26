print('=' * 30)
print('{:^30}'.format('Banco do Trembolouco'))
print('=' * 30)
valor = int(input('digite o valor que voce quer sacar r$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print('Total de {} cedulas de r${}.'.format(totalced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
