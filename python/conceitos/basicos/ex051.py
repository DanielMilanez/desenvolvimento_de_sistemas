# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progreção aritimetica). No final, mostre os
# 10 primeiros termos desta progressão.

print('Lendo uma P.A. progreção aritmetica')
num = int(input('Digite o valor do primeiro termo desta PA: '))
raz = int(input('Agora, digite o valor da razão desta PA: '))

print('Os 10 primeiros termos desta progressão são:')
for i in range(0, 10):
    print(num, end=' ')
    num += raz
