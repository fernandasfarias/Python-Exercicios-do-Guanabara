numeros = ()
for i in range(4):
    num = int(input(f'Digite o número da posição {i + 1}: '))
    numeros += (num, )
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
        print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado.')
print('Os números pares foram: ',end='')
for item in numeros:
    if item % 2 == 0:
        print(f'{item}',end=' ')
