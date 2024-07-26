listagem_de_produtos = ('arroz', 10, 'feijao', 25, 'batata', 2, 'beringela', 3, 'quiabo', 4)
print('==' * 30)
print(f"{'supermercados Trembolouco':^60}")
print('==' * 30)
print("Produto\t..........\tPreço") 

for produto, preco in zip(listagem_de_produtos[::2], listagem_de_produtos[1::2]):

    print("{: <10}..........R$:{: >5}".format(produto, preco))