from time import sleep
def contador():
    for numero in range(1, 11):  # Use colon (:) to start a function or loop block
        sleep(0.3)
        print(numero)


print('Contagem de 1 ate 10:')
contador()

def doisemdois():
    for numero in range(10, 0, -2):
        if numero % 2 == 0:
            sleep(0.3)
            print(numero)


print('Contagem regressiva de 2 em 2: ')
doisemdois()



def aleatorio():
    a = int(input('Início: '))
    b = int(input('Fim: '))
    passo = int(input('Passo: '))

    if passo == 0:
        print("O passo não pode ser zero. Verifique os valores informados.")
        return

    if b < a:
        # Contagem regressiva: subtrai 'passo' de 'a' até chegar a 'b'
        print(f"Contagem regressiva de {a} até {b}, subtraindo {passo} em cada etapa:")
        while a > b:
            sleep(0.3)
            print(a)
            a -= passo
        # Garante que 'a' não fique abaixo de 'b'
        if a < b:
            a = b  # Define 'a' como 'b' para encerrar a contagem
    else:
        # Contagem progressiva: soma 'passo' a 'a' até chegar a 'b'
        print(f"Contagem progressiva de {a} até {b}, somando {passo} em cada etapa:")
        while a < b:
            sleep(0.3)
            print(a)
            a += passo
        # Garante que 'a' não ultrapasse 'b'
        if a > b:
            a = b  # Define 'a' como 'b' para encerrar a contagem

    print(a)  # Imprime o último valor (b) alcançado na contagem

aleatorio()