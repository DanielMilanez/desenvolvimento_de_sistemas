link_arquivo = '.\prova\\arquivo_da_prova.json'
import json
from os import system, path

calculo = {
    'operacao': [],
    'num1': [],
    'num2': [],
    'resultado': []
}
system('cls')

if not path.exists(link_arquivo):
    with open(link_arquivo, 'a', encoding='utf-8') as resposta:
        json.dump(
            calculo,
            resposta
        )

with open(link_arquivo, 'r') as resposta:
    results = json.load(resposta)

operandos = ['+', '-', '*', '/']
print('==' * 10, 'CALCULADORA', '==' * 10)

def salvar(result, operacao, num1, num2):
    results['operacao'].append(operacao)
    results['resultado'].append(result)
    results['num1'].append(num1)
    results['num2'].append(num2)

    with open(link_arquivo, 'w', encoding='utf-8') as resposta:
        json.dump(
            results,
            resposta
        )

    print('\033[32mO calculo foi salvo com sucesso!\033[m')

def calculadora(operacao):
    result = 0
    try:
        num2 = float(input('Informe o segundo número: '))
        match operacao:
            case '+':
                result = num1 + num2
                print(f'O resultado é: {result}') 
            case '-':
                result = num1 - num2
                print(f'O resultado é: {result}')
            case '*':
                result = num1 * num2
                print(f'O resultado é: {result}')
                
            case '/':
                result = num1 / num2
                print(f'O resultado é: {result}')
        
    except ZeroDivisionError:
        print('Não é possível realizar uma divisão por 0')
        result = 'Divisão por 0'
    
    salvar(result, operacao, num1, num2)

def exibir():
    op = ''
    op += '('

    for i in operandos:
        op += f'{i} '

    op += '): '
    return op

num1 = float(input('Informe o primeiro número: '))
op = input(f'Informe a operação: {exibir ()} ')

for i in operandos:
    if op == i:
        calculadora(op)
        break
