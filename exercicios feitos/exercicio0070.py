numero = ( 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero_inserido = int(input('Digite um numero de 1 a 20: '))

while numero_inserido > 20 or numero_inserido < 1:
    numero_inserido = int(input('Digite um numero de 1 a 20: '))

print(numero[numero_inserido -1])