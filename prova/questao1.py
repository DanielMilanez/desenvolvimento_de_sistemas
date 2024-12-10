from os import system

system('cls')

def classificar_idade(idade):
    if idade < 12:
        return 'Criança'
    elif idade <= 17:
        return 'Adolecente'
    elif idade >= 18:
        return 'Adulto'

for i in range(3):
    idade = int(input('Informe sua idade >> '))
    print(f'Você é: {classificar_idade(idade)}')
