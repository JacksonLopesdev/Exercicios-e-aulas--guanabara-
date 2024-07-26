while True:
    numero = int(input('Digite um numero para eu lhe dar a tabuada: '))
    if numero >= 0:
        for i in range(1, 11):
            resultado = numero * i
            print('{} x {} = {}'.format(numero, i, resultado))
    else:
        print('ta bom parei !')