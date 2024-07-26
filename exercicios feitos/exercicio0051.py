#for n in range(0,501):
#    n %3 == 0:
#    print('A soma de todos os valores divisiveis por 3, de 1 a 500 e de: {}'.format(sum(n)))

soma = 0
cont = 0
for n in range(1, 501, 2):  
    if n % 3 == 0:  
        soma += n #a soma vai acumulando, ou seja, cada vez que acha, ela soma o valor junto aos anteriores
        cont += 1 #isso e um contador, ele soma mais um a cada vez que acha um numero impar divisivel por 3 na lista citada
print('A soma de todos os {} valores impares, divisíveis por 3, de 1 a 500, é: {}'.format(cont, soma))
