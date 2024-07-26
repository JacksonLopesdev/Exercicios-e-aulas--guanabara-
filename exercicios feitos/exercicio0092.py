def area(a, b):
    resultado = (a * b)  
    print('-'*50)
    print(f'A area do seu terreno e de: {resultado} metros quadrados.')
    print('-'*50)


print('Controle de terrenos !')
print('-'*50)
largura = float(input('Digite a largura do terreno(M):')) 
comprimento = float(input('Digite o comprimento do terreno(M):'))
area(largura, comprimento)