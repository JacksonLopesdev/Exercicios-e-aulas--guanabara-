linhas = 3
colunas = 3
matriz_vazia = [[0] * colunas for _ in range(linhas)]

for linha in range(linhas):
    for coluna in range(colunas):
        numero_adicionado = int(input('Digite 9 numeros para eu adicionar em uma matriz 3 x 3: '))
        matriz_vazia[linha][coluna] = numero_adicionado

for l in matriz_vazia:
    print(l)

soma_terceira_coluna = sum(matriz_vazia[i][2] for i in range(linhas))

print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')

soma_pares = sum(valor for linha in matriz_vazia for valor in linha if valor % 2 == 0)

print(f'A soma dos valores pares da matriz é: {soma_pares}')

segunda_linha = matriz_vazia[1]
maior_valor_segunda_linha = max(segunda_linha)

print(f'O maior valor da segunda linha é: {maior_valor_segunda_linha}')