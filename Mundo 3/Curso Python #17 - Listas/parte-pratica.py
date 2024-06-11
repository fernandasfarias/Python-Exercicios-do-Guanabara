num = [2, 5, 9, 1]
print(type(num))
num[2] = 7 
# Adicionar ao final da lista
num.append(8)
# Colocar em ordem crescente 
num.sort() 
# Colocar em ordem decrescente
num.sort(reverse=True) 
print(num)
# Inserir valores
num.insert(2, 0) # Na posição 2, inserir o número 0
print(num)
# Eliminar elementos
num.pop(2) # Sem parâmetro, elimina o último. Porém, podemos especificar o índice
if 8 in num:
    num.remove(8) # Outra forma de remover.
else:
    print('Número não encontrado na lista')
print(num)
# Quantidade de elementos
print(f'Essa lista tem {len(num)} elementos') 

valores = list()
valores.append(5)
valores.append(4)
valores.append(9)

for pos, valor in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {valor}!')
for valor in valores:
    print(f'{valor}...',end='')
print()
numeros = list()
for cont in range(0, 6):
    numeros.append(int(input('Digite um valor: ')))
print(numeros)

# Ligação de uma lista
a = [9, 8, 4, 3]
b = a
b[0] = 1
print(f'Lista A: {a}') # Ao modificar em uma, modifico na outra
print(f'Lista B: {b}')

# Copiar uma lista através do fatiamento
c = [99, 55, 66]
d = c[:]
d[1] = 33
print(f'Lista C: {c}')
print(f'Lista D: {d}')
