# ler 3 numeros e mostrar o maior

val = input('Digite 3 números separados por / para saber qual o maior: ')
lista = val.split('/')
a, b, c = map(int, lista)

if a > b and a > c:
    maior = a
elif b > c:
    maior = b
else:
    maior = c

print(f'O maior número é {maior}')
