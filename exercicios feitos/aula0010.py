#nome = str(input('qual seu nome ?')).strip().lower()
#if nome == 'gustavo'.lower():
#    print('que nome lindo voce tem')
#else:
#    print('seu nome e tao normal')
#print('bom dia, {}!'.format(nome))
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n = (n1 + n2) /2
if n <5.0:
    print('sua media foi de: {}, precisa melhorar !!'.format(n))
else:
    print('sua media foi de: {}, parabens, esta no caminho certo !!'.format(n))
#print('a sua media e de: {}.'.format(n))