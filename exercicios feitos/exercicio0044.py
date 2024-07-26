altura = float(input('Digite sua altura (em metros): '))
peso = int(input('Digite seu peso (em kg): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('abaixo do peso.')
elif 18.5 >= imc < 25:
    print('peso ideal.')
elif 25 <= imc < 30:
    print('sobrepeso.')
elif 30 <= imc < 40:
    print('obesidade.')
else:
    print('obesidade morbida.')