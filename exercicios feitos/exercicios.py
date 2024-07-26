

#1 - Escreva um programa que receba uma lista de números e retorne a soma de todos os elementos da lista.

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for som in numeros:
#    soma = sum(numeros)
#print(soma)

#2 - Crie uma função que receba uma lista de palavras e retorne outra lista com o comprimento de cada palavra.

# Define uma lista de palavras
palavras = ["python", "programação", "lista", "exercícios", "fixação"]

# Cria uma lista vazia para armazenar os comprimentos das palavras
comprimento = []

# Inicia um loop que itera sobre cada palavra na lista de palavras
for palavra in palavras:
    # Para cada palavra na lista de palavras, obtém o comprimento da palavra
    tamanho = len(palavra)
    # Adiciona o comprimento da palavra à lista de comprimentos
    comprimento.append(tamanho)

# Após o término do loop, imprime a lista de comprimentos
print(comprimento)
