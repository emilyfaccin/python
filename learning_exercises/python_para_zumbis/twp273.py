# ler 4 notas, exibir notas e media na tela

print('Digite o valor das notas separadas por "/" para obter a média:')
val = input()
notas = [float(i) for i in val.split('/')]

soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)

print(f'As notas obtidas foram {notas}, obtendo média {media}')
