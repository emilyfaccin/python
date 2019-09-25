'''populacao de A 80000 com crescimento de 3% e B 200000 com crescimento
    1,5% ao ano. escrever o numero de anos necessarios para que A iguale
    ou ultrapasse B'''

a = 80000
b = 200000
ano = 0
while(a < b):
    a *= 1.03
    b *= 1.015
    ano += 1

print(
    f'{ano} ano(s) é o tempo necessário para que a população de A se iguale '
    'ou supere a população de B.'
)
