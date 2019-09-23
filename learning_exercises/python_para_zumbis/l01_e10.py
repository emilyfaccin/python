# calcular a reducao do tempo de vida de um fumante
# ler cigarros fumados por dia e tempo em anos como fumante
# -10 minutos/cigarro, exibir em dias

print('Digite o total de cigarros fumados por dia:')
cigarro = int(input())
print('Agora digite os anos como fumante: ')
anos = float(input())

total = (anos * 365 * cigarro * 10) / 1440

print(f'Sua vida foi reduzida em {total:.0f} dias. Pare de fumar!')
