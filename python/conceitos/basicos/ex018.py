# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
num = float(input('Informe um angulo: '))

seno = math.sin(math.radians(num))
coseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))

print('Valor em radianos')
print('O valor do seno deste ângulo é: {:.2f}'.format(coseno))
print('O valor do cosseno deste ângulo é: {:.2f}'.format(seno))
print('O valor da tangente deste ângulo é: {:.2f}'.format(tangente))
