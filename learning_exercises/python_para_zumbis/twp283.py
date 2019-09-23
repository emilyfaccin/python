# ler uma palavra e trocar vogais por *

print('Digite uma palavra para trocar as vogais por *:')
palavra = input()

i = 0
for i in range(len(palavra)):
    if palavra[i] in 'aeiou':
        palavra = palavra[:i] + '*' + palavra[i + 1:]

# Também possível assim =)
# for c in 'aeiou':
#     nome = nome.replace(c, "*")

print(f'A palavra modificada é {palavra}')
