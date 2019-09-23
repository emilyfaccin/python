# calcular o aumento de salario, recebendo salario atual e o percentual
# de aumento

print('Digite o salario e o percentual de aumento, separados por [/]: ')
valor = input()
lista = valor.split('/')

percent = float(lista[1])
print(percent)
sal = float(lista[0])
sal = sal * (1 + percent / 100)
print(sal)

print(f'O novo salário após o aumento de {percent:.1f}% é de R$ {sal:.2f}')
