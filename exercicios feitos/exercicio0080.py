lista = []
lista_par = []
lista_impar = []

while True:
    adicionado = int(input('Digite um numero: '))
    parar = input('Deseja continuar ? [s/n]: ').strip().lower()

    lista.append(adicionado)
    if adicionado % 2 == 0:
        lista_par.append(adicionado)

    elif adicionado % 2 == 1:
        lista_impar.append(adicionado)
    if parar == 's':
        continue
    elif parar == 'n':
        break


print(f'{lista}\n{lista_par}\n{lista_impar}')