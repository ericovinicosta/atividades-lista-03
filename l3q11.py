"""
    11. Altere o programa anterior para mostrar no final a soma dos números.
"""
start_serie = int(input('Informe o inicio da serie: '))
end_serie = int(input('Informe o fim da serie: '))

soma = 0

print(f'Serie [{start_serie}:{end_serie}]')
for numero in range(start_serie,end_serie):
    soma += numero
print(soma)