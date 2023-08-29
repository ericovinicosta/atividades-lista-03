'''
8. Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
quantidade_numeros = 5
soma = 0

for num in range(quantidade_numeros):
    soma += float(input('Digite um numero: '))
    
print(f'Total da soma é: {soma:2}')
print(f'A média é: {soma/quantidade_numeros:2}')