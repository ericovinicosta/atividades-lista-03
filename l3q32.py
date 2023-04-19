"""32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
        a. Fatorial de: 5
           5! =  5 . 4 . 3 . 2 . 1 = 120
"""

numero = int(input('Número: '))

print(f'Fatorial de: {numero}')
fat = 1

print(f'{numero}! =', end='')
for n in range(numero,0,-1):
    if n != 1:
        print(f' {n} .', end='')
    else:
        print(f' {n} = ', end='')
    fat *= n

print(fat)