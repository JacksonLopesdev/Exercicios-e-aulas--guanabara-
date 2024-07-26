def factorial(n, mostrar_passo_a_passo=False, nivel_recursao=0):
    # Verifica se n é 0 ou 1 (caso base)
    if n == 0 or n == 1:
        # Se mostrar_passo_a_passo for True, mostra o passo base
        if mostrar_passo_a_passo:
            print(f"{'  ' * nivel_recursao}{n}! = 1")
        return 1  # Retorna 1 para 0! e 1!

    # Calcula o fatorial de n - 1 recursivamente
    resultado_n_menos_1 = factorial(n - 1, mostrar_passo_a_passo, nivel_recursao + 1)

    # Calcula o fatorial de n multiplicando n pelo fatorial de n - 1
    resultado = n * resultado_n_menos_1

    # Se mostrar_passo_a_passo for True, mostra o passo atual do cálculo
    if mostrar_passo_a_passo:
        print(f"{'  ' * nivel_recursao}{n}! = {n} * ({n - 1}!) = {resultado}")

    return resultado  # Retorna o resultado do fatorial de n

# Função para calcular e mostrar ou não o processo do fatorial
def calcular_e_mostrar_fatorial(numero, mostrar_passo_a_passo=False):
    # Verifica se devemos mostrar o início do cálculo
    if mostrar_passo_a_passo:
        print(f"Cálculo do fatorial de {numero}:")

    # Chama a função factorial para calcular o fatorial do número
    resultado_fatorial = factorial(numero, mostrar_passo_a_passo)

    # Verifica se devemos mostrar apenas o resultado final
    if not mostrar_passo_a_passo:
        print(f"O fatorial de {numero} é {resultado_fatorial}")

# Exemplo de uso:
numero = 5
calcular_e_mostrar_fatorial(numero, mostrar_passo_a_passo=True)  # Mostra o processo passo a passo
calcular_e_mostrar_fatorial(numero, mostrar_passo_a_passo=False)  # Mostra apenas o resultado final
