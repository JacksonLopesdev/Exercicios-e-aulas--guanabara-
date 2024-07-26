s = float(input('Digite o seu salario que irei calcular um aumento, vc e merecedor guerreiro:'))
p = float(input('Quantos por cento de aumento esse guerreiro merece ?'))
pa = (s*p) /100
ar = s + pa
print('seu salario base era de {} reais, voce como um bom moço, merecedor, ganhou {} por cento de aumento, sendo a porcentagem em reais de {}, seu salario a partir de hoje fica {} reais.'.format(s,p,pa,ar))
