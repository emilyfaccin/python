# ler 5 numeros e printar a lista

print('Digite cinco números separados por /: ')
val = input().split('/')
lista = list(map(int, val))
print(f'Vetor lido: {lista}')
