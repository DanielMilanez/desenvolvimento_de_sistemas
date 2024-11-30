# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão

# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número inteiro qualquer: '))
convert = int(input('Agora selecione a base de conversão (1-binário | 2-octal | 3-hexadecimal): '))

if convert == 1:
    num = bin(num)[2:]
    print('A conversão para número binário será: {}'.format(num))
elif convert == 2:
    num = oct(num)[2:]
    print('A conversão para número octal será: {}'.format(num))
elif convert == 3:
    num = hex(num)[2:]
    print('A conversão para número hexadecimal será: {}'.format(num))
