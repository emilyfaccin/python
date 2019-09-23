# ler 10 numeros reais e mostrar na ordem inversa

print('Digite 10 numeros separados por /:')
val = input()
lista = [float(i) for i in val.split('/')]
lista.reverse()

print(f'O reverso da lista inserida é {lista}')
