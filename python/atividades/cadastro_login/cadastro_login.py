import cadastrados as cad

print('==' * 10, 'LOGIN', '==' * 10)
opition = input('O que você deseja (l - para o login / c - cadastro ) >> ')

match opition:
    case 'l':
        login = input('Informe seu login: ')
        senha = input('Informe sua senha: ')
        cad.login(login, senha)
    case 'c':
        login = input('Informe seu novo login: ')
        senha = input('Informe sua nova senha: ')
        cad.cadastro(login, senha)
    case _:
        print('Opição inválida!') 
