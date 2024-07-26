preco_normal = float(input('Preço do produto: '))
cp = int(input('Digite o número da condição de pagamento:\n1- À vista.\n2- À vista no cartão.\n3- Em 2x no cartão.\n4- 3x no cartão: '))

if cp == 1:
    valor_com_desconto = preco_normal - (0.1 * preco_normal)
    print('O valor com desconto de 10% será de: {}'.format(valor_com_desconto))
elif cp == 2:
    valor_com_desconto = preco_normal - (0.05 * preco_normal)
    print('O valor à vista no cartão será de: {}'.format(valor_com_desconto))
elif cp == 3:
    valor_com_desconto = preco_normal
    print('O valor em 2x no cartão será de: {}'.format(valor_com_desconto / 2))
elif cp == 4:
    valor_com_desconto = preco_normal + (0.2 * preco_normal)
    print('O valor em 3x no cartão será de: {}'.format(valor_com_desconto / 3))
else:
    print('Condição de pagamento inválida.')
