from os import system 
saldo = 200
system('cls')

while True:
    try:
        opition = int(input('1 - SACAR \n2 - SALDO \n0 - SAIR \n>> '))
        
        match opition:
            case 0: 
                print('Fim da operação')
                break
            case 1:
                try:
                    valorSaque = int(input('Informe o valor a ser sacado >> '))
                    
                    if valorSaque > saldo:
                        raise Exception
                    
                    elif valorSaque < 0:
                        raise Exception
                    
                    else:
                        saldo -= valorSaque
                        print(f'O valor R$ {valorSaque} foi sacado!')
    
                except Exception:
                    print('OPERAÇÃO INVÁLIDA!')  
                      
                except ValueError as Error:
                    print(f'OPERAÇÃO INVÁLIDA! Insira um valor adequado. Código do erro\033[31m {Error}\033[m')          
                                    
            case 2:
                print(f'O saldo disponível é de R${saldo}')
            case _:
                system('cls')
                print(f'\033[31mOpção inválida\033[m tente novamente.')
                
    except ValueError as Error:
        print(f'Operação inválida, insira um valor adequado. Código do erro\033[31m {Error}\033[m')
    
    except Exception as Error:
        print(f'Erro inesperado ocorreu, \033[31m{Error}\033[m')
    
    finally:
        print(f'Saldo atual {saldo}')     
