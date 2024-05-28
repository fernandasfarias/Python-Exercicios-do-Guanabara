num_por_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numero = int(input('Digite um número entre de 0 a 20: '))
while not 0 <= numero <= 20:
    numero = int(input(('Tente novamente. Digite um número de 0 a 20: ')))
for pos, num in enumerate(num_por_extenso):
    if pos == numero:
        print(f'O número por extenso é: {num}')
        break
