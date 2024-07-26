import datetime

dados = {}

dados['Nome'] = input('Nome: ')

data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
data_atual = datetime.datetime.now()
dados['idade'] = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

dados['carteira'] = input('Número da carteira de trabalho: ')
if dados['carteira'] == '0':  
    del dados['carteira']
dados['ano_contratacao'] = input('Ano de contratação: ')

ano_contratacao = int(dados['ano_contratacao'])
dados['ano_aposentadoria'] = ano_contratacao + 35

print('Aqui estao seus dados: ')
print(dados)
print('-'*90)
for chave, valor in dados.items():
    print(chave + ':', valor)
