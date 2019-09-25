# receber dois numeros inteiros positivos e determinar o maior divisor
# comum entre eles usando o algoritmo de Euclides

print('Digite dois números para encontrar o maior divisor comum entre eles:')
a = int(input('1:'))
b = int(input('2:'))

while a % b != 0:
    a, b = b, a % b

print(f'O MDC entre os numeros digitados é {b}')
