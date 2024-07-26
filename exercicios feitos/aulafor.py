# Definindo uma lista
numeros = [1, 2, 3, 4, 5]

# Iterando sobre a lista e imprimindo cada elemento
for numero in numeros:
    print(numero)


# Exemplo de uso do laço for para percorrer uma lista
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)


# Definindo uma string
palavra = "Python"

# Iterando sobre a string e imprimindo cada caractere
for letra in palavra:
    print(letra)


# Iterando sobre um intervalo de números de 1 a 10
for i in range(1, 11):
    print(i)


# Exemplo 1: Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print("Eu gosto de", fruta)

# Exemplo 2: Iterando sobre uma string
mensagem = "Olá, mundo!"
for caractere in mensagem:
    print(caractere)

# Exemplo 3: Iterando sobre um dicionário
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for chave, valor in pessoa.items():
    print(chave + ":", valor)

# Exemplo 4: Usando a função range()
for i in range(1, 6):  # Vai de 1 a 5
    print(i)


# Definindo uma lista
frutas = ['maçã', 'banana', 'laranja', 'morango']

# Iterando sobre a lista e imprimindo tanto o índice quanto o valor
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")


