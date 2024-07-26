try:
    a = int(input('n1'))
    b = int(input('n2'))
    r = a/b
except (ValueError, TypeError):
    print('deu bom nao man')
else:
    print(f'resultado {r}')

