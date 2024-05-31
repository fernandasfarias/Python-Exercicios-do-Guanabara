# Importar a biblioteca random para gerar os números aleatórios.
from random import randint 

# Criar a tupla com os 5 números aleatórios.
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# Imprimir cada um desses números na tela.
print('Os números escolhidos foram: ', end='')
for num in numeros:
    print(f'{num}', end=' ')

# Encontrar o maior e o menor valor da tupla. 
maior_num = menor_num = numeros[0]
for num in numeros[1:]:
    if num > maior_num:
        maior_num = num
    if num < menor_num:
        menor_num = num
print(f'\nO maior número foi: {maior_num}')
print(f'O menor número foi: {menor_num}')
