# calcular o fatorial de um numero inteiro n

n = int(input('Digite um número para calcular seu fatorial: '))
fat = 1
cont = 2

while cont <= n:
    fat *= cont
    cont += 1

print(f'O valor de {n}! é de {fat}')

# calcular a soma de numeros inteiros até que seja digitado 0
soma = 0
while True:
    n = int(input('Digite numeros a serem somados. Para terminar digite 0.\n'))
    if n == 0:
        break
    soma += n
print(f'A soma resultou em : {soma}')