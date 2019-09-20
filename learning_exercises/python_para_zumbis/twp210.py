#ler um numero e imprimir os pares entre zero e esse numero

num = int(input('Digite um numero: '))
x = 0

while(x <= num):
    if x % 2 == 0:
        print(x)
    x += 1