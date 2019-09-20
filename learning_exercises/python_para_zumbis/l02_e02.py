# determine se um ano é bissexto

''' é multiplo de 400
    é multiplo de 4 e não é multiplo de 100 '''

ano = int(input('Digite o ano para verificar se é bissexto: '))

if ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
elif ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')