'''ler usuario e senha digitados e não aceitar senha igual ao nome de
    usuário, mostrando mensagem de erro e pedindo dados novamente'''

while True:
    print('Digite usuário e senha, separados por /.', end=' ')
    print('A senha não poderá ser igual ao usuário!',)
    user, senha = input().split('/')
    if user != senha:
        break
print(f'Usuario: {user}, Senha: {senha}')
