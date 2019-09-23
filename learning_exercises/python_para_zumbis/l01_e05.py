# ler preco e percentual de desconto / exibir desconto e preco final

print('''Insira o valor original do produto e o percentual de desconto,
    separados por "/": ''')

val = input()
lista = val.split('/')

desc = float(lista[1])
preco = float(lista[0]) * (1 - desc / 100)

print(
    f'''O desconto concedido foi de {desc:.1f}%, resultando no valor
    final de R$ {preco:.2f}''')
