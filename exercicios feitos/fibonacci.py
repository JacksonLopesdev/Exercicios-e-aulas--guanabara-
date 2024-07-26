a = 0 #primeiro numero da sequencia
b = 1 #segundo numero da sequencia
fibonacci = [] #lista vazia para eu poder adicionar
termos = int(input('digite quantos termos voce quer q eu calcule em uma sequencia de fibonacci: '))
for i in range(termos): #montamos um laco por que nao sabemos de quanto sera o input
    if i == 0:
        fibonacci.append(a) #se for igual a 0 adicionar a 
    elif i == 1:
        fibonacci.append(b) #se for igual a 1 adicionar o b
    else:
        proximo_numero = a + b #aqui vem o pulo do gato, tenho que criar uma variavel para o proximo numero, 
        fibonacci.append(proximo_numero) #aqui adicionamos o proximo termo a lista, ele e variavel entao depende do input
        a = b #caracterizamos isso, para usar como parametro a soma com o anterior, assim o computador entende
        b = proximo_numero #aqui caracterizamos o proximo numero
        print('A sua sequencia fibonacci fica assim: {}'.format(fibonacci))
        