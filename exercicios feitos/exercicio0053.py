soma = 0
cont = 0
for i in range(6):
    i = int(input('digite 6 numeros para mim, farei a soma de todos os pares para voce: '))
    if i % 2 == 0:
        soma += i
        cont += 1

print('a soma de todos os {} numeros pares e de: {}'.format(cont, soma))
