'''ler peso dos peixes. se exceder 50.0 kg armazenar na variavel
    excedente (quantidade de kg acima) e multa (valor total da
    multa cobrada / R$ 4 por kg excedente) caso não haja excesso,
    excedente e multa devem estar zeradas'''

peso = float(input('Digite o total pescado em kg: '))

if peso > 50:
    exced = peso - 50
    multa = int(exced) * 4.00
else:
    exced = multa = 0

print(
    f'''O total de {peso:.2f} kg pescados excedeu em {exced:.2f} kg o
    permitido, gerando uma multa de R$ {multa:.2f}.'''
)
