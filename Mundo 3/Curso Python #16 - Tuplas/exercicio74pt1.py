from random import randint
numeros_aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números escolhidos foram:', end=' ')
for num in numeros_aleatorios:
    print(f'{num}', end=' ')
print(f'\n O maior número foi: {max(numeros_aleatorios)}')
print(f'O menor número foi: {min(numeros_aleatorios)}')
