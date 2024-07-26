nome = str(input('digite seu nome completo:')).strip()
mai = nome.upper()
min = nome.lower()
lat = len(nome.replace(' ',''))
lpf = nome.split()[0]
#tambem posso usar o count acima, e citar o primeiro espaco colocando o sinal de menos nele.
lpn = len(lpf)
print('aqui esta: seu nome completo em letras maiusculas: {}.\nTodas em minusculas: {}.\nQuantas letras tem: {}.\nE quantas letras tem seu primeiro nome:{}'.format(mai,min,lat,lpn))
#posso atribuir tudo ao print no .format, mas prefiro atribuir antes.