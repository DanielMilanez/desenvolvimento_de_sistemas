# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número: '))
contador_de_divisiveis = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end=' ')
        contador_de_divisiveis += 1
    else:
        print('\033[31m', end=' ')

    print('{}'.format(i), end=' ')

print()
if contador_de_divisiveis > 2:
    print('\033[mEle não é primo')
else:
    print('\033[mEle é primo')
