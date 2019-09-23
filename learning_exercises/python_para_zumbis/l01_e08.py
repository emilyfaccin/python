# ler uma temperatura em farenheit e transformar em celsius f = 9 * c / 5 + 32

print('Digite a temperatura em Celsius a ser convertida para Celsius: ')

farenheit = float(input())
celsius = (farenheit - 32) * 5 / 9

print(f'A temperatura digitada em Celsius é de {celsius} °C.')
