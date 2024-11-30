# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# para salários superios a 1.250, calcule um aumento de 10%, para inferiores ou iguais, o aumento é de 15%

salario = float(input('Informe o salário do funcionário: R$'))

if salario <= 1.250:
    salario = salario + (salario * (15 / 100))
else:
    salario = salario + (salario * (10 / 100))

print('Quem ganhava {0} passa a ganhar {0}'.format(salario))
