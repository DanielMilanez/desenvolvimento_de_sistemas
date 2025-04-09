# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Informe seu salário atual: R$'))

reajuste = salario * (15 / 100)
salario_final = salario + reajuste

print('Seu novo salário, com o reajuste de 15% ficará: R${0:.2f}'.format(salario_final))
