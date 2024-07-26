#for c in range(1, 10):
#    print(c)
#print('fim')


#c = 1
#while c < 10:
#    print(c)
#    c += 1
#print('fim')

#n = 1
#while n != 0:
#    n = int(input('digite um numero: '))
#print('fim')

#r = 's'
#while r == 's':
#    n = int(input('Digite um numero: '))
#    r = str(input('Quer continuar ? [s,n] ')).lower().strip()
#print('Fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1

print('voce digitou {} numeros pares, e {} numeros impares.'.format(par, impar))

