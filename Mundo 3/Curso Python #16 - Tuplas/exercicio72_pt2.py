num_por_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if not  0 <= num <= 20:
        print('Tente novamente.', end=' ')
    else:
        print(num_por_extenso[num])
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar == 'N':
            break
