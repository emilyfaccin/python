# ler três números e mostrar o maior e o menor

print('''Digite 3 números para saber qual o maior e o menor dentre eles,
    usando / como separador: ''')
val = input()
lista = val.split('/')
a, b, c = map(int, lista)

menor = a
maior = b

if a > b:
    maior, menor = a, b
    if c > a and c > b:
        maior = c
    elif c < b and c < a:
        menor = c
elif c < a and c < b:
    menor = c
if c > a and c > b:
    maior = c

print(f'O maior número digitado é {maior} e o menor é {menor}')
