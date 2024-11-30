# Escreva um programa que faça o computador "penasr" entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador, o programa deverá escrever na tela se o usuário venceu ou perdeu

import random

print('DESCUBRA O NÚMERO QUE ESTOU PENSANDO :3')
number_pc = random.randint(0, 5)
num = int(input('Número (0 a 5): '))

if number_pc == num:
    print('PARABÉNS você acertou!')
else:
    print('OPS! Você errou!')

print('Meu número era {}'.format(number_pc))
