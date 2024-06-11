produtos = ('Lápis de olho Boca Rosa', 49.90, 'Gloss Labial Max Love', 13.98, 'Battom Matte Anita', 14.86, 'Esmalte preto Impala', 5.63, 'Kit Mari Maria Makeup', 88.90)
print('-'*144)
print(f'{'Produtos mais vendidos no setor maquiagem':^135}')
print('-'*144)
for pos, item in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{item:.<35}', end='')
    else:
        print(f'R${item:>6.2f}')
print('-'*144)
