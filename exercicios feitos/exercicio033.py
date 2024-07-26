v = int(input('qual distancia voce pretende viajar ? '))
if v <= 200:
    print('o preco da sua viajem e igual a: {}'.format(v*0.50))
else:
    print('o preco da sua viajem e igual a: {}'.format(v*0.45))