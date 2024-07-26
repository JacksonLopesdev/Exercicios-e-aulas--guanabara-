d = int(input('Quantos dias voce ficou com o veiculo ?'))
km = float(input('Qauntos kilometros voce rodou com o mesmo ?'))
al = (d * 60) + (km * 0.15)
print('voce ficou {} dias e andou {} km com o veiculo, portanto o valor do seu aluguel e de: {}'.format(d, km, al))
