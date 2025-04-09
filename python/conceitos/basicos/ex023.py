# faça um programa que leia um número de 0 a 9.999 e mostre na tela cada um dos dígitos separados!
# ex: milhar: 1 centena: 8 dezena: 3 unidade: 4

num = input('Digite um número [0 a 9.999]: ')
num = ' '.join(num)

num = num.split()
print('Milhar: {}'.format(num[0]))
print('Centena: {}'.format(num[1]))
print('Dezena: {}'.format(num[2]))
print('Unidade: {}'.format(num[3]))
