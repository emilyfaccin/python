# média de 5 notas

print('Digite 5 notas em sequência separadas por "/" para obter a média:')
val = input().split('/')
lista = list(map(float, val))
i = 0
soma = 0

for n in lista:
    soma += n

print(f'A média das notas digitadas é {soma/len(lista)}')
