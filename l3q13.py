"""
13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""
base = int(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))

print(f'{base:2} ^ {expoente:2} = {base**expoente}')