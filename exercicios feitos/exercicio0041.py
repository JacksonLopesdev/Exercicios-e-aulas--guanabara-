from datetime import date, datetime, timedelta

dia = int(input('Digite sua data de nascimento, dia: '))

while dia < 1 or dia > 31:
    print('Dia inválido, por favor digite o dia correto.')
    dia = int(input('Digite sua data de nascimento, dia: '))

mes = int(input('Mês (números): '))
while mes < 1 or mes > 12:
    print('Mês inválido, digite o mês correto.')
    mes = int(input('Mês (números): '))

ano = int(input('Ano: '))
while ano < 1920 or ano > date.today().year:
    print('Ano inválido, digite o ano correto.')
    ano = int(input('Ano: '))

data_nascimento = date(ano, mes, dia)
dia_atual = date.today()

diferenca = dia_atual - data_nascimento

if diferenca.days / 365.25 < 18:
    print('Você não precisa se alistar ainda!')

elif diferenca.days / 365.25 > 19:
    print('seu tempo ja passou !!')

else:
    print('Você precisa se alistar no exército brasileiro!')
