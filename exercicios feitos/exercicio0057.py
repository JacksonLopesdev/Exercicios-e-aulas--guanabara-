from datetime import date

idades = [] #definindo idades como lista, para poder printar as 7 la embaixo

for _ in range(7):
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

    idade_float = diferenca.days / 365.25

    if idade_float < 18:
        print('Você tem {:.0f} anos, e ainda não é maior de idade!'.format(idade_float))
    else:
        print('Você tem {:.0f} anos, já é maior de idade!'.format(idade_float))

    idade_int = int(idade_float + 0.5) 
    idades.append(idade_int)

print("Idades das 7 pessoas, respectivamente: {}".format(idades))
