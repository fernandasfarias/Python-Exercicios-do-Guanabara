from random import randint 
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os números escolhidos foram: ', end='')
for num in numeros:
    print(f'{num}', end=' ')
maior_num = menor_num = numeros[0]
for num in numeros[1:]:
    if num > maior_num:
        maior_num = num
    if num < menor_num:
        menor_num = num
print(f'\nO maior número foi: {maior_num}')
print(f'O menor número foi: {menor_num}')
