"""
12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    a. Tabuada de 5:
        5 X 1 = 5
        5 X 2 = 10
        ...
        5 X 10 = 50
"""
tabuada = int(input('Informe o numero para gerar a tabuada: '))

print(f'Tabuada de {tabuada}:')
for numero in range(10):
    print(f'{tabuada:2} x {(numero + 1):2} = {(tabuada * (numero + 1)):2}')