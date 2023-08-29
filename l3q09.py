'''
    9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
for numero in range(1,50):
    if numero % 2 == 1 :
        print(f'{numero}', end=' ')
print(end='\n')