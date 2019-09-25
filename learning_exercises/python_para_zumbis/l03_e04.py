# ler um numero e calcular seu Fibonacci

print('Digite um número para calcular seu Fibonacci: ')
n = int(input())

result = 0
a = 0
b = 1

for i in range(n):
    b, a = a, a + b

print(f'O Fibonacci na {n}ª posição é {a}')
