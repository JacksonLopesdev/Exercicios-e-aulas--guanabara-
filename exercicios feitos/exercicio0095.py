def maior_valor():
    contador = 0
    valores = []  # Lista para armazenar os valores informados

    while True:
        entrada = int(input('Informe um valor (ou 0 para parar): '))
        
        if entrada == 0:
            break  # Encerra o loop se o usuário digitar 'p' para parar

        try:
            valores.append(entrada)  # Adiciona o valor à lista de valores
            contador += 1  # Incrementa o contador de valores informados
        except ValueError:
            print('Entrada inválida. Por favor, informe um número inteiro ou "0" para parar.')

    if valores:
        maior = max(valores)  # Encontra o maior valor na lista de valores informados
        print(f'Você informou {contador} valores e o maior deles foi {maior}!')
    else:
        print('Nenhum valor foi informado.')

maior_valor()