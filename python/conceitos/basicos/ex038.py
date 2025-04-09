# escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem

# o primeiro valor é maior
# o segundo valor é maior
# não existe valor maior, os dois são iguais

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))

if num1 > num2:
    print('{0} é maior que {1}'.format(num1, num2))
elif num1 < num2:
    print('{0} é menor que {1}'.format(num1, num2))
else:
    print('NÃO EXISTE valor maior, os dois são IGUAIS!')
