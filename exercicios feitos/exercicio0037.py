r1 = int(input('Digite o tamanho de 3 retas para mim, eu direi se elas formam um triangulo ou nao, primeira: '))
r2 = int(input('segunda: '))
r3 = int(input('terceira: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('voce pode formar um triangulo com essas linhas !!')
else:
    print('essas retas nao podem formar um triangulo.')
