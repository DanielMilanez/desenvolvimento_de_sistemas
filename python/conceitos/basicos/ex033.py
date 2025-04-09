# faça um programa que leia três números e mostre qual é o mairo e qual é o menor

num1 = int(input('Insira um valor: '))
num2 = int(input('Insira um valor: '))
num3 = int(input('Insira um valor: '))

menor = num1
maior = num1

if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3

# Verificando quem é o maior

if num2 > num1 and num2 > num3:
    maior = num2

if num3 > num1 and num3 > num2:
    maior = num3

print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))
