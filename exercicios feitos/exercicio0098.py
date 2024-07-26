from datetime import date

def calcular_idade():
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento
        return idade
    except ValueError:
        print("Ano de nascimento inválido. Por favor, digite um número inteiro.")
        return None

def voto():
    idade = calcular_idade()
    if idade is not None:
        if idade >= 18 and idade < 65:
            print('Seu voto é obrigatório.')
        elif idade >= 65:
            print('Seu voto é opcional.')
        else:
            print('Voto não obrigatório.')

# Chamar a função voto para verificar o status do voto
voto()
