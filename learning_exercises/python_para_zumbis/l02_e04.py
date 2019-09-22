# ler 3 numeros e mostrar o maior

val = input('Digite 3 números separados por / para saber qual o maior: ')
lista = val.split('/')
a, b, c = map(int, lista)

maior = a
if b > a:
    if c > b:
        maior = c
    else:
        maior = b
elif c > a:
    maior = c

print(f'O maior número é {maior}')