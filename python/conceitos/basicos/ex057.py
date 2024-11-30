# Faça um programa que leia o sexo de um pessoa, mas só aceite os valores M ou F.
# caso esteja errado, peça a digitação novamente até t er um valor correto

sex = input('Digite o sexo (M ou F): ').strip().lower()
validation = sex == 'm' or sex == 'f'

while not validation:
    print('\033[31mValores inválidos!\033[m Por favor digite novamente: ', end='')
    sex = input().strip().lower()
    validation = sex == 'm' or sex == 'f'

print('\033[32mObrigado por colaborar :)')
