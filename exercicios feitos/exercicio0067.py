nome = []
idade = []
sexo = []

while True:

    n = input('Digite seu nome: ').strip().lower()
    i = int(input('Digite sua idade: '))
    s = input('Qual seu sexo? (m) ou (f): ').strip().lower()
    idade.append(i)
    nome.append(n)
    sexo.append(s)
    resposta = input('deseja continuar ? (s, ou n para nao:): ')
    if resposta == 's':
        continue
    else:
        break

maiores_de_18 = 0
homens = 0
mulheres_menores_20 = 0


for idx, valor_idade in enumerate(idade):
    if idade[idx] >= 18:
        maiores_de_18 += 1
        

    if idade[idx] < 20 and sexo[idx] == 'f':
        mulheres_menores_20 += 1
        

    if sexo[idx] == 'm':
        homens += 1
        

print('{} pessoas sao maiores de 18 anos.'.format(maiores_de_18))
print('{} mulheres abaixo de 20 anos !'.format(mulheres_menores_20))
print('{} homens na lista.'.format(homens))