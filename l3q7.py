'''
    7. Faça um programa que leia 5 números e informe o maior número.
'''
maior = 0
for n in range(1,6):
    numero = int(input('Digite um número: '))
    if n == 1:
        maior = numero
    else:
        if numero > maior:
            maior = numero

print(f'O maior número é: {maior}')