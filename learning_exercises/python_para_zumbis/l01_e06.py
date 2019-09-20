# ler distancia e velocidade media e calcular tempo de viagem

val = input('Digite a distância a ser percorrida e a velocidade média esperada durante a viagem, separados por "/": ')

lista = val.split('/')
horas = int(float(lista[0]) / float(lista[1]))
minutos = float(lista[0]) % float(lista[1])

print(f'Com base nos dados fornecidos, o tempo de viagem esperado é de {horas} horas e {minutos:.0f} minutos.')