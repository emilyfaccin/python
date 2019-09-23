# verificar se uma palavra é palindrome (minusculo sem acento)

print('Digite uma palavra para verificar se é palíndrome:')
palavra = input()

if palavra == palavra[::-1]:
    print(f'{palavra} é palíndrome.')
else:
    print(f'{palavra} não é palíndrome.')
