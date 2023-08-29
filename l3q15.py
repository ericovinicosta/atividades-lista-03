'''15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.'''

num1 = 1
num2 = quantidade = 0
n = int(input('Digite o limite da sequência: '))
for quantidade in range(n+1):
    numero = num1 + num2
    print(f'{numero}', end=' ')
    num1 = num2
    num2 = numero
    quantidade += 1
print()