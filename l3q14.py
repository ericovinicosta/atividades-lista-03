"""
    14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""

quantidade_pares = 0
quantidade_impares = 0

for num in range(10):
    numero = int(input('Digite um numero: '))
    if numero % 2:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

print(f'quantidade de pares: {quantidade_pares}')
print(f'quantidade de impares: {quantidade_impares}')