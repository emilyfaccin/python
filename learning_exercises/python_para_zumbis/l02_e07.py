'''ler tamanho em m2. cobertura da tinta é de 1L por 3m2 / tinta é vendida
    em latas de 18L que custa R$ 80. informar qtde de latas necessárias'''


print('Informe a área a ser pintada, em metros quadrados: ')
area = float(input())

# cada litro de tinta pinta 03 metros quadrados
litro = area / 3

# se os litros necessarios forem multiplos de 18
if litro % 18 == 0:
    # basta dividir por 18 pra encontrar o numero de latas de tinta
    lata = litro / 18
# caso contrário
else:
    # divide-se o total de litros necessários por 18 e soma 01 ao resultado
    lata = litro // 18 + 1
print(f'Serão necessárias {lata} latas de tinta, a um custo de R${lata * 80}.')
