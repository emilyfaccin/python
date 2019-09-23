# pedir os 3 lados de um triangulo. informar se pode ser um triangulo e
# caso possa, se é equilatero, isóceles ou escaleno

print('Digite as 3 medidas dos lados dos triangulos, separados por / : ')
lados = input()
lista = lados.split('/')

a, b, c = map(int, lista)

if a + b < c or b + c < a or a + c < b:
    print('Essas medidas não podem formar um triângulo.')
else:
    if a == b == c:
        print('Essas medidas formam um triângulo equilátero.')
    elif a == b or a == c or b == c:
        print('Essas medidas formam um triângulo isóceles.')
    else:
        print('Essas medidas formam um triângulo escaleno.')
