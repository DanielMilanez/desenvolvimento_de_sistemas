# Crie um programa que faça o computador jogar jokenpô com você

import random
from time import sleep

print('VAMOS JOGAR!')
print('-=' * 11)
player = input('Pedra, Papel ou Tesoura: ').lower()
lista_de_jogadas = ['pedra', 'papel', 'tesoura']

escolha_do_computador = random.choice(lista_de_jogadas)

print('JO ', end='')
sleep(1)
print('KEN ', end='')
sleep(1)
print('PÔ')
sleep(.5)

if player == 'pedra' or player == 'papel' or player == 'tesoura':
    print('-=' * 11)
    print('MINHA ESCOLHA FOI: \033[33m{} \033[0m'.format(escolha_do_computador))
    print('SUA ESCOLHA FOI: \033[32m{} \033[0m'.format(player))
    print('-=' * 11)

    print('O resultado é: ', end='')
    if escolha_do_computador == player:
        print('EMPATE!')

    elif (escolha_do_computador == 'pedra' and player == 'papel') or \
            (escolha_do_computador == 'papel' and player == 'tesoura') or \
            (escolha_do_computador == 'tesoura' and player == 'pedra'):
        print('VOCÊ GANHOU!')

    else:
        print('EU GANHEI!')

else:
    print('Valores inválidos, insira apenas pedra, papel ou tesoura')
