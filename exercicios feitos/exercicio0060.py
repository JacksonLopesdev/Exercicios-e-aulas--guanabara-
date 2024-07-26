sexos = {'m': 'masculino', 'f': 'feminino'}

while True:
    sexo = input('Informe o seu sexo (m ou f): ').strip().lower()
    if sexo in ['m', 'f']:
        break  
    else:
        print('Erro, digite novamente: m para masculino, e f para feminino.')

print('Sexo:', sexos[sexo])

