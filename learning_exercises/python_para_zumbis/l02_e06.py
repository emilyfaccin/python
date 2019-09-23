'''ler salario/hora e horas trabalhadas. calcular e mostrar o total do
salario do mes sao descontados 11% de IR, 8% de INSS e 5% sindicato.
Mostrar salario bruto descontos e salário líquido'''

print('Digite o valor recebido por hora:')
sal_hora = float(input())
print('Agora, digite o total de horas trabalhadas: ')
hora_trab = float(input())

sal_bruto = sal_hora * hora_trab
ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sind = sal_bruto * 0.05

sal_liq = sal_bruto - ir - inss - sind

print(
    f'''Tabela Salarial:
    + Salário Bruto: R$ {sal_bruto:.2f}
    - IR (11%): R$ {ir:.2f}
    - INSS (8%): R$ {inss:.2f}
    - Sindicato (5%): R$ {sind:.2f}
    = Salário Líquido: R$ {sal_liq:.2f}
''')
