nome = input('digite seu nome completo:').strip()
partes = nome.split()
pn = partes[0]
un = partes[-1]
print('seu primeiro nome e: {}.\nSeu ultimo nome e:{}.'.format(pn,un))
#nome = input('digite seu nome completo:').strip()
#print('Seu primeiro nome e: {}.'.format(nome.split()[0]))
#print('seu ultimo nome e: {}.'.format(nome.split()[-1]))