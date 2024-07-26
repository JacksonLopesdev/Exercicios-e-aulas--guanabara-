#pt = int(input('digite o primeiro termo da sua progressao aritmetica: ' ))
#razao = int(input('agora digite a razao da mesma: '))

#ut = pt + (10 - 1) * razao #isso e a equacao matematica para calcular o ultimo termo da pa

#for pa in range(pt, ut, razao):
#    print(pa, '->')

numero = []

pt = int(input('Digite o primeiro termo da sua pa: '))
razao = int(input('Digite a razao da mesma: '))

numero.append(pt)

while True:
    pt = pt + razao
    numero.append(pt)
    proximo = input("Deseja adicionar o próximo termo? (s/n): ")
    print(pt)
    if proximo.lower() != 's':
        break

for termo in numero:
    print(termo)