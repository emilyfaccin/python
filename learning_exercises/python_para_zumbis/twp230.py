# 01 ler um numero do usuario e imprimir os numeros impares de 1 até o numero
# 02 imprimir os 10 primeiros multiplos de 3
# 03 calcular a média de 10 numeros inteiros


# 01
num = int(input('Digite um numero: '))
x = 1
while x <= num:
    print(x)
    x += 2

# 02
cont = 1
while cont <= 10:
    print(cont * 3)
    cont += 1

# 03
cont = 0
soma = 0
while cont < 10:
    soma += int(input('Digite um numero: '))
    cont += 1
print(soma/cont)