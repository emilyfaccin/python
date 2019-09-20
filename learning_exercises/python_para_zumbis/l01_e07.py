# converter uma temperatura recebida em celsius para farenheit f = 9 * c / 5 + 32

celsius = float(input('Digite a temperatura em Celsius a ser convertida para Farenheit: '))

print('A temperatura digitada em Farenheit é de {} °F.' .format(celsius * 9 / 5 + 32))