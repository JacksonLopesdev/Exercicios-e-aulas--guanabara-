palavras = ('livro', 'remedio', 'gramado', 'namorada', 'mulher', 'esposa', 'ronaldo', 'brilha', 'muito', 'no', 'corinthians')

vogais = ('a', 'e', 'i', 'o', 'u')  

for palavra in palavras:
    vogais_na_palavra = [vogal for vogal in vogais if vogal in palavra]
    print(f"{palavra}: {', '.join(vogais_na_palavra)}")
