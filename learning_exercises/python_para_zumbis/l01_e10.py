# calcular a reducao do tempo de vida de um fumante
# ler cigarros fumados por dia e tempo em anos como fumante
# -10 minutos/cigarro, exibir em dias

cigarro = int(input('Digite o total de cigarros fumados por dia para calcular a redução do tempo de vida:'))
anos = float(input('Agora digite os anos como fumante: '))

total = (anos * 365 * cigarro * 10) / 1440

print(f'Sua vida foi reduzida em {total:.0f} dias. Pare de fumar!')