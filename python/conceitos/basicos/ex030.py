# Faça um programa que diga se um número é par ou não

num = int(input('Digite um número: '))
calc = num % 2

if calc != 0:
    print('O número é impar! ')
else:
    print('O número é par!')
