''' ler uma nota entre 0 e 10, mostre uma mensagem caso o valor seja
    inválido e continue pedindo até que o usuário informe um valor
    válido '''

while True:
    print('Digite uma nota entre 0 e 10:')
    nota = float(input())
    if 0 <= nota <= 10:
        break
print(f'A nota digitada é {nota}')
