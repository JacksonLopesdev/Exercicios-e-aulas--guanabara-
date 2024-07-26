print('Olá, sou seu gerente de financiamentos,'
      ' vi que voce esta procurando financiar uma casa, para isso,'
      ' voce precisara me responder algumas perguntas ok ?')

salario_mensal = float(input('muito bem vamos la: qual seu salario mensal ?:'))

valor_casa = float(input('Qual valor total do financiamento ?:'))

anos_parcela = float(input('Em quantos anos voce pretende parcelar esse financiamento ?:'))

meses_parcela = anos_parcela * 12

valor_mensalidade = valor_casa / meses_parcela

if valor_mensalidade >= 0.3 * salario_mensal:

    print('Seu financiamento nao pode ser aprovado, devido ao valor da mensalidade ser muito alto.')

else:
    print('Parabens, seu financiamento foi aprovado, e o valor da sua mensalidade e de:''{:.2f}'.format(valor_mensalidade))