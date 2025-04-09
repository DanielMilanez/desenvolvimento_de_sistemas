# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa

from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digita o valor do cateto adjacente: '))

# Função que calcula a hipotenusa
hi = hypot(co, ca)

print('O comprimento da hipotenusa é: {:.f2}'.format(hi))
