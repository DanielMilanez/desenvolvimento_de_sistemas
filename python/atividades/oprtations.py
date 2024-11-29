from os import system

def operation(num1, num2, operacao):
    match operacao:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '/':
            return num1 / num2
        case '*':
            return num1 * num2
        case _:
            return 'invalido'
    
while True:
    system('cls')
    print('==' * 10, 'Operações', '==' * 10)
    num1 = float(input('Informe um número: '))
    num2 = float(input('Informe outro número: '))
    try:    
        print('Operações disponíveis')
        print('+  para somar')
        print('-  para subitrair')
        print('/ para dividir')
        print('* para multiplicar')
        
        operacao = input('Informe a operação desejada >> ')
        result = operation(num1, num2, operacao)
        
        if result == 'invalido':
            print('Operação inválida!')
            continue
        
        print(f'O resultado da operação é: {result}')
        verify = input('deseja continuar? ')
        
        if verify == 'n': 
            print('Fim da operação')
            break
        
    except ZeroDivisionError:
        print('Operação inválida!')
        continue
