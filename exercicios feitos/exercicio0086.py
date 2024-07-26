ficha = list()

while True:
    nome = str(input('nome: '))
    nota_1 = float(input('nota 1: '))
    nota_2 = float(input('nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    continuar = str(input('Quer continuar ? [s/n] '))
    if continuar in 'n':
        break

print('*-' * 30 )
print(f'{"no.":<4}{"nome":<10}{"media":>8}')
print('__' * 30 )
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opc = int(input('Mostrar notas de qual aluno ? [999 para parar]'))
    if opc == 999:
        print('Ate mais ze cu !!!')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<<Volte sempre >>>')
