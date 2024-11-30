# Desenvolva um programa que faça uma contagem regressiva

from time import sleep

print('Contagem!')
print('=-' * 11)

for i in range(10, -1, -1):
    sleep(1)
    print('\033[0;32m{}\033[0m'.format(i), end=' ')

print('LANÇAR!')
print('=-' * 11)
