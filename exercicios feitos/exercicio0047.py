#transformando numeros em binario, octal, e hexadecimal
numero = int(input('Digite um numero inteiro: '))
print("""escolha uma das bases para conversao)
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL""")
opcao = int(input('Sua opcao:'))
if opcao == 1:
    print('{} convertido para BINARIO e igual a: {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('{} convertido para OCTAL e igual a: {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL e igual a: {}'.format(numero, hex(numero)))
else:
    while True:
        print('Opcao invalida, tente novamente.')
        opcao = int(input('Sua opcao:'))

        if opcao == 1:
            print('{} convertido para BINARIO e igual a: {}'.format(numero, bin(numero)))
            break

        elif opcao == 2:
            print('{} convertido para OCTAL e igual a: {}'.format(numero, oct(numero)))
            break

        elif opcao == 3:
            print('{} convertido para HEXADECIMAL e igual a: {}'.format(numero, hex(numero)))
            break

