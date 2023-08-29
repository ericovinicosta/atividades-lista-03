"""
10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""
start_serie = int(input('Informe o inicio da serie: '))
end_serie = int(input('Informe o fim da serie: '))

print(f'Serie [{start_serie}:{end_serie}]')
for numero in range(start_serie,end_serie):
    print(numero, end=' ')