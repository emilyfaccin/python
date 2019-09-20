# ler uma temperatura em farenheit e transformar em celsius, sendo f = 9 * c / 5 + 32

farenh = float(input('Digite a temperatura em Celsius a ser convertida para Celsius: '))

print('A temperatura digitada em Celsius é de {} °C.' .format((farenh -32) * 5 / 9))