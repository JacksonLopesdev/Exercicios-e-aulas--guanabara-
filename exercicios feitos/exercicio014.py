p = float(input('digite o preço do protduto:'))
p1 = float(input('muito bem, agora digite quantos por cento de desconto tem, somente o numero por favor:'))
d = (p*p1) /100
pt = p - d
print('seu produto custa {} reais, e tem {}% de desconto, que e {} reais, e custara depois do desconto:{:.2f}'.format(p,p1,d,pt))

