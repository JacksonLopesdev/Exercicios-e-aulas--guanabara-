nome = str(input('Qual e o seu nome ?')).strip().lower()
if nome == 'gustavo':
    print('que nome em !!')
elif nome == 'jackson':
    print('seu nome e fenomenal man na moral que delicia,',nome)
elif nome in 'ana claudia jessica juliana':
    print('nome razoavel')
elif nome == 'tamara' or nome == 'costa' or nome == 'vaca':
    print('que delicinha em', nome)
else:
    print('Seu nome e uma bosta gatao!!')
    print('Tenha um otimo dia !', nome)
