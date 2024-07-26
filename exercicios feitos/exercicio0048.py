import string
from time import sleep
from emoji import emojize
f = emojize(":sparkler:")
print('Preparem-se: contagem regressiva para os fogos de fim de ano !!')
texto = '10 9 8 7 6 5 4 3 2 1 0'
temp = ''
for m in texto:
    for i in string.printable:
        if i == m or m == i:
            sleep(0.009)
            print(temp + i)
            temp += m
            break
        else:
            sleep(0.009)
            print(temp + i)
print(f)
print('__|__')










#for c in range(10, -1, -1):

    #sleep(1)

    #print('contagem regressiva: {}'.format(c))
#print(f)
#contagem regressiva de 10 ao 0 com 1 segundo de delay e colocando emoji para o estouro boom