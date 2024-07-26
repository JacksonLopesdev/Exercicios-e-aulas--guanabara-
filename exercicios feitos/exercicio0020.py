import math
ag = float(input('Digite um angulo qualquer que eu irei lhe dizer o seno, cosseno, e tangente do mesmo:'))
ar = math.radians(ag)
s = math.sin(ar)
c = math.cos(ar)
t = math.tan(ar)
print('O seno do angulo {}, e igual a:{}.\nO cosseno e igual a:{}.\nA tangente e igual a:{}.'.format(ag, s, c, t))