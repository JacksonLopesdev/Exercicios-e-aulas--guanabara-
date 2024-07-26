def notas(*n, sit=False):
    """
    --> funcao para analisar as notas, tendo medias, 
    maior, menor e tudo mais, no caso do sit,
    adicionei valor boleano ao mesmo, para caso a pessoa chame
    a funcao, ela apareca, caso nao, ela fique irrelevante.
    return: dicionario com varias paradas.
    """
    r= dict() 
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoavel'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5, 8.9, 7.5, 5, 2, 4, 2.1, sit=True)
print(resp)
help(notas)
