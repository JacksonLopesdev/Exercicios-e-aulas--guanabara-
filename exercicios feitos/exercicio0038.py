nome = str(input('Olá, sou a calculadora de financiamentos criada por Jackson Lopes. Aqui consulto financiamentos com taxa de juros variável, salário variável e valor do imóvel variável. Vamos começar? Primeiro, me diga seu nome: ')).strip().lower()

salario = float(input('Muito bem, {} agora seu salário mensal: '.format(nome)))

valor_casa = float(input('Qual valor a ser financiado: '))

taxa_de_juros = float(input('Perfeito, me diga a taxa de juros mensais em porcentagem, incluído como valor percentual; ex: (60% = 0.60), do financiamento que estamos simulando: '))

tipo_de_amortizacao = str(input('Defina o modelo de amortização para mim, ele pode ser no modelo "price" ou "sac", caso queira calcular as duas, digite o valor "0": ')).strip().lower()

num_parcelas = int(input('Me diga em quantas parcelas será feito o financiamento: '))

limite_mensalidade = 0.3 * salario

print('Lembrando que nesse modelo, a mensalidade do financiamento não pode ultrapassar 30% do valor da mensalidade.')

def sac(valor_casa, taxa_de_juros, num_parcelas):
    amortizacao = valor_casa / num_parcelas
    juros_total = 0
    total_pago = 0
    parcelas = []
    saldo_devedor = valor_casa

    for _ in range(num_parcelas):
        juros = saldo_devedor * taxa_de_juros
        saldo_devedor -= amortizacao
        parcela = amortizacao + juros
        total_pago += parcela
        parcelas.append((amortizacao, juros, parcela))
        juros_total += juros

    return parcelas, juros_total, total_pago

def price(valor_casa, taxa_de_juros, num_parcelas):
    parcela = valor_casa * (taxa_de_juros /(1 - (1 + taxa_de_juros) ** - num_parcelas))
    juros_total = 0
    total_pago = 0
    saldo_devedor = valor_casa
    parcelas = []

    for _ in range(num_parcelas):
        juros = saldo_devedor * taxa_de_juros
        amortizacao = parcela - juros
        saldo_devedor -= amortizacao
        parcela = amortizacao + juros
        total_pago += parcela
        parcelas.append((amortizacao, juros, parcela))
        juros_total += juros

    return parcelas, juros_total, total_pago

if tipo_de_amortizacao == 'sac':
    parcelas_sac, juros_total_sac, total_pago_sac = sac(valor_casa, taxa_de_juros / 12, num_parcelas)
    mensalidade_sac = sum([parcela[2] for parcela in parcelas_sac]) / num_parcelas
    if mensalidade_sac <= limite_mensalidade:
        print('\nModelo SAC (para financiamento de casa):')
        print('parcelas amortizacao juros parcela total')
        for i, (amortizacao, juros, parcela) in enumerate(parcelas_sac, start=1):
            print(f'parcela {i}: {amortizacao:.2f}    {juros:.2f}    {parcela:.2f}')
        print(f'mensalidade: {mensalidade_sac:.2f}')
        print(f'total de juros: {juros_total_sac:.2f}')
        print(f'o valor que você pagará no total será de {total_pago_sac:.2f}')
        print("Mensalidades:")
        print([parcela[2] for parcela in parcelas_sac])
    else:
        print("A mensalidade do financiamento SAC ultrapassa 30% do seu salário.")
        salario_minimo_sac = total_pago_sac / (0.3 * num_parcelas)
        print(f'Para obter o financiamento SAC, você precisaria de um salário mínimo de {salario_minimo_sac:.2f}.')

elif tipo_de_amortizacao == 'price':
    parcelas_price, juros_total_price, total_pago_price = price(valor_casa, taxa_de_juros / 12, num_parcelas)
    mensalidade_price = sum([parcela[2] for parcela in parcelas_price]) / num_parcelas
    if mensalidade_price <= limite_mensalidade:
        print("\nModelo Price (para um financiamento de casa):")
        print("Parcelas Amortização    Juros   Parcela Total")
        for i, (amortizacao, juros, parcela) in enumerate(parcelas_price, start=1):
            print(f"Parcela {i}:  {amortizacao:.2f}     {juros:.2f}      {parcela:.2f}")
        print(f"Total de Juros: {juros_total_price:.2f}")
        print(f"Mensalidade: {mensalidade_price:.2f}")
        print(f"O valor que você pagará no total será de {total_pago_price:.2f}")
        print("Mensalidades:")
        print([parcela[2] for parcela in parcelas_price])
    else:
        print("A mensalidade do financiamento Price ultrapassa 30% do seu salário.")
        salario_minimo_price = total_pago_price / (0.3 * num_parcelas)
        print(f'Para obter esse financiamento, você precisaria de um salário mínimo de {salario_minimo_price:.2f}.')

elif tipo_de_amortizacao == '0':
    parcelas_sac, juros_total_sac, total_pago_sac = sac(valor_casa, taxa_de_juros / 12, num_parcelas)
    parcelas_price, juros_total_price, total_pago_price = price(valor_casa, taxa_de_juros / 12, num_parcelas)
    mensalidade_sac = sum([parcela[2] for parcela in parcelas_sac]) / num_parcelas
    mensalidade_price = sum([parcela[2] for parcela in parcelas_price]) / num_parcelas
    if mensalidade_sac <= limite_mensalidade and mensalidade_price <= limite_mensalidade:
        print("\nModelo SAC (para um financiamento de casa):")
        print("Parcelas Amortização    Juros   Parcela Total")
        for i, (amortizacao, juros, parcela) in enumerate(parcelas_sac, start=1):
            print(f"Parcela {i}:  {amortizacao:.2f}     {juros:.2f}      {parcela:.2f}")
        print(f"Total de Juros (SAC): {juros_total_sac:.2f}")
        print(f"Mensalidade (SAC): {mensalidade_sac:.2f}")
        print(f"O valor que você pagará no total será de {total_pago_sac:.2f}")
        print("Mensalidades:")
        print([parcela[2] for parcela in parcelas_sac])

        print("\nModelo Price (para um financiamento de casa):")
        print("Parcelas Amortização    Juros   Parcela Total")
        for i, (amortizacao, juros, parcela) in enumerate(parcelas_price, start=1):
            print(f"Parcela {i}:  {amortizacao:.2f}     {juros:.2f}      {parcela:.2f}")
        print(f"Total de Juros (Price): {juros_total_price:.2f}")
        print(f"Mensalidade (Price): {mensalidade_price:.2f}")
        print(f"O valor que você pagará no total será de {total_pago_price:.2f}")
        print("Mensalidades:")
        print([parcela[2] for parcela in parcelas_price])
    else:
        print("As mensalidades dos financiamentos SAC e Price ultrapassam 30% do seu salário.")
        salario_minimo_sac = total_pago_sac / (0.3 * num_parcelas)
        salario_minimo_price = total_pago_price / (0.3 * num_parcelas)
        print(f'Para obter o financiamento SAC, você precisaria de um salário mínimo de {salario_minimo_sac:.2f}.')
        print(f'Para obter o financiamento Price, você precisaria de um salário mínimo de {salario_minimo_price:.2f}.')

else:
    print('Opção de modelo de amortização inválida. Por favor, escolha "sac", "price" ou "0".')
