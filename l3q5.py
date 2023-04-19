"""5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação."""

while(True):
    contador = 0
    A = int(input('Digite a população para A: '))
    if A == 0:
        break
    B = int(input('Digite a população para B: '))
    if B ==0:
        break
    taxa_a = float(input('Informe a taxa de crescimento para A: '))
    taxa_b = float(input('Informe a taxa de crescimento para B: '))

    while(A < B):
        A += A * taxa_a/100
        B += B * taxa_b/100
        contador += 1

    print(f'Passaram {contador} anos')
    print(f'A = {int(A)} e B = {int(B)}')