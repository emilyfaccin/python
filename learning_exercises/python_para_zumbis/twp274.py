# ler 10 caracteres minusculos e dizer quantas consoantes foram lidas

print('Digite 10 caracteres minúsculos para saber quantos são consoantes:')
val = input()
lista = [i for i in val.split('/')]

cont = 0
for i in lista:
    if i not in 'aeiou':
        cont += 1

print(f'Existem {cont} consoantes dentre os caracteres digitados.')
