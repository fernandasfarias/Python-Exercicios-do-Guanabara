palavras = ('garrafa', 'borracha', 'sabonete', 'condicionador', 'maquiagem', 'mouse', 'estojo', 'cadeira', 'toalha', 'penteadeira', 'borrifador', 'abajur')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
