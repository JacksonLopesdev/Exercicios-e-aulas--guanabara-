frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:  
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")

#frase[:]: Isso indica que estamos acessando toda a string.
#frase[::]: Aqui, o primeiro dois-pontos : indica o início, e o segundo dois-pontos : indica o fim. Como eles estão em branco, isso significa que estamos acessando toda a string.
#frase[::1]: O terceiro parâmetro 1 indica o passo ou o intervalo entre os caracteres. Um passo de 1 significa que estamos pegando cada caractere na ordem original.
#frase[::-1]: Agora, mudando o passo para -1, estamos percorrendo a sequência de trás para frente, ou seja, invertendo-a.