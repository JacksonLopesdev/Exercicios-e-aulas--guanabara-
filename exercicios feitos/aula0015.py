#pessoas = {'nome': 'gustavo', 'sexo' : 'M', 'idade' : 22}
#del pessoas ['sexo'] deleta a parte sexo do dicionario todo
#pessoas['nome'] = 'Leandro' tranformar o nome em leandro
#pessoas['peso] = 95 adiciona um item ao dicionario, nao preciso dar append pois nao funciona
#for k in pessoas.keys():
#for k, v in pessoas.items(): aqui declaro os dois valores, pois items e para os dois
  #  print(k)
#.keys() seria o primeiro valor ou seja, nome, sexo, idade 
#.values() seria o segundo valor, ou seja, gustavo, m, 22
#.items() imprime todos

#brasil = []
#estado1 = {'uf': 'Rio de janeiro', 'sigla' : 'RJ'}
#estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]["uf"])

estado = dict()  #dict e dicionario !
brasil = list()  #list e lista !

for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:   #esse for e para a lista
    #for k, v in e.items():   esse for e para os valores unidade federativa e sigla
        #print(f'o campo {k} tem valor {v}')
    for v in e.values():
        print(v, end=' ') #o end e a msm coisa que o \n
    print()