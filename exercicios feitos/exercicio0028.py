frase = input('digite uma frase:').strip().upper()
qv = frase.find('A') + 1
q = frase.count('A')
qf = frase.rfind('A') + 1
if qv !=-1 and qf !=-1:
    print('A letra a aparece o total de: {}.\nO local que ela aparece a primeira vez e {}.\nO local onde aparece por ultimo e {}.'.format(q,qv,qf))
else:
    print('a letra nao foi encontrada')
#frase = str(input('digite sua frase:').upper()
#print('a letra a aparece {} vezes na frase.'.format(frase.count('A')))
#print('a primeira letra a apareceu na posicao:'.format(frase.find('A')+1))
#print('a ultima letra a da frase esta na posicao {}.'.format(frase.rfind('A')+1))
#duas formas de fazer !!!