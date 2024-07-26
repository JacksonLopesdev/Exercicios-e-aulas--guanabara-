idade = int(input('digite sua idade: '))
if idade < 9:
    print('Categoria: Mirim.')
elif 9 >= idade < 14:
    print('Categoria: Infantil.')
elif 14 <= idade < 19:
    print('categoria: Junior.')
elif 19 <= idade < 20:
    print('Categoria: Sênior.')
else:
    print('Categoria: Master.')