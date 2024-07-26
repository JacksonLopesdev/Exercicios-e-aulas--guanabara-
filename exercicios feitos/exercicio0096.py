from random import randint

numeros = []
pares = []

def sorteio():
    for _ in range(5):
        aleatorio = randint(1, 100)
        numeros.append(aleatorio)
        if aleatorio % 2 == 0:
            pares.append(aleatorio)

sorteio()  
print(f'Números sorteados: {numeros}')  

def somapar():
    soma = sum(pares)
    print(f'A soma dos números pares é: {soma}')

somapar()  
