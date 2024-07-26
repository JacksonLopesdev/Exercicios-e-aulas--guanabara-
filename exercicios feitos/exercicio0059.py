nome = []
idade = []
sexo = []

for _ in range(4):
    n = input('Digite seu nome: ').strip().lower()
    i = int(input('Digite sua idade: '))
    s = input('Qual seu sexo? (m) ou (f): ').strip().lower()
    idade.append(i)
    nome.append(n)
    sexo.append(s)

media = sum(idade) / 4
maior_idade = max(idade)

print('A média de idade do grupo é de {} anos.'.format(media))

for idx, valor_idade in enumerate(idade):
    if sexo[idx] == 'f' and valor_idade < 20:
        print('{} tem menos de vinte anos!'.format(nome[idx]))
    elif valor_idade == maior_idade and sexo[idx] == 'm':
        print('{} tem a maior idade entre os homens!'.format(nome[idx]))