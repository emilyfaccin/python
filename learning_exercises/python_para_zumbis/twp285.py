# recebe uma data e imprime o mês por extenso

print('Digite sua data de nascimento no formato dd/mm/aaaa:')
data = [int(i) for i in input().split('/')]

meses = [
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
    'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
]
# procura na lista "meses" qual item tem o indice igual ao mes digitado - 1
# (já que a lista começa com indice 0)
print(f'O mês por extenso da data digitada é {meses[data[1] - 1]}')
