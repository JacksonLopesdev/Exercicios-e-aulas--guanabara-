v = float(input('velocidade atual do veiculo: '))
if v <= 80:
    print('meus parabens, voce respeita os limites de velocidade impostos para sua seguranca.')
else:
    m = (v - 80) * 7
    print('voce nao respeita os limites de velocidade, sera multado e o valor da sua multa e de:',m)
