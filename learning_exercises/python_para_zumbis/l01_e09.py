# le quantidade de km rodados e dias de locacao de carro e calcula o 
# preco a pagar, sendo 60.00/dia e 0.15/km rodado

val = input('Digite a quilometragem rodada durante o aluguel e os dias de locação (separados por "/"): ')

lista = val.split('/')

valor = float(lista[0]) * 0.15 + float(lista[1]) * 60

print(f'O valor total a ser pago é de {valor}.')