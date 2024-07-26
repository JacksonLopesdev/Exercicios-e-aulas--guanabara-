from datetime import date
ano = int(input('digite um ano qualquer e lhe direi se e bissexto ou nao, ou, coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 00:
    print('Esse ano e bissexto !!')
else:
    print('esse ano nao e bissexto !!')