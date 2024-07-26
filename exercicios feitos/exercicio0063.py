numero = []
digitados = int(input('digite um numero, para parar digite 999:'))
while digitados != 999:
    digitados = int(input('digite um numero, para parar digite 999:'))
    numero.append(digitados)
    soma = sum(numero) - 998
print(soma)
