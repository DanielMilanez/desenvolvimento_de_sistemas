import cadastrados as cad

print('==' * 10, 'aurora.com.br', '==' * 10)
opition = input('O que você deseja (l - para o login / c - cadastro ) >> ')

while True:
    match opition:
        case 'l':
            login = input('Informe seu login: ')
            senha = input('Informe sua senha: ')
            cad.login(login, senha)
            break

        case 'c':
            login = input('Informe seu novo login: ')
            
            while True:
                senha = input('Informe sua nova senha: ')
                confirm_senha = input('Confirme a senha: ')
                    
                if not senha == confirm_senha:
                    print('\033[31mAs senhas não são iguais\033[m')
                    continue
                else:
                    cad.cadastro(login, senha)

                break
            print('Login criado com sucesso!')
            break
        case _:
            print('\033[31mOpição inválida!\033[m') 
