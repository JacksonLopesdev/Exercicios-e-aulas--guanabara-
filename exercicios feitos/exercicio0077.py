numeros = []

while True:
    adicionado = input('Digite um numero(para parar digite sair): ')
    if adicionado == 'sair':
        break

    elif int(adicionado) not in numeros:
        numeros.append(int(adicionado))

    numeros.sort()

print(numeros)

