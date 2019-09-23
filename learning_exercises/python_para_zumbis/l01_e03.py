# ler qtde de dias, horas, min e seg do usuario e transformar tudo em seg

print(
    '''Digite a quantidade a ser transformada obedecendo a seguinte ordem:
    DD:HH:mm:ss''')
qtde = input()
lista = qtde.split(':')
dia = int(lista[0])
hora = int(lista[1])
minuto = int(lista[2])
segundo = int(lista[3])

total_seg = dia*24*60*60 + hora*60*60 + minuto*60 + segundo

print('O total é de %d segundos' % total_seg)
