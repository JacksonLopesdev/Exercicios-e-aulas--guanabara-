lista_1 = []
lista_2 = []

expressao = input('digite uma expressao: ')
parentese_a = '('
parentese_f = ')'

for i in expressao:
    if i == parentese_a:
        lista_1.append(parentese_a)
    elif i == parentese_f:
        lista_2.append(parentese_f)

if len(lista_1) == len(lista_2):
    print('A expressao esta correta.')

else:
    print('A expressao ta uma merda, da um jeito nesses parenteses ai chará !!!')