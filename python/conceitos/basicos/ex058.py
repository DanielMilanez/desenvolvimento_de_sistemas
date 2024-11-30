#  Melhore o jogo do desafio 28 onde o computaodr vai "pensar" em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print()
print('Estou pensando em um número de 0 a 10, consegue adivinhar qual é?')
print('=' * 65)

palpite = 0
entrada = int(input('Digite seu chute: '))

numero_computador = randint(0, 10)

print('=' * 65)

while entrada != numero_computador:
    if entrada < numero_computador:
        print('\033[31mVOCÊ ERROU!\033[m Tente novamente, é\033[33m maior\033[m do que {}: '.format(entrada), end='')
    elif entrada > numero_computador:
        print('\033[31mVOCÊ ERROU!\033[m Tente novamente, é\033[33m menor\033[m do que {}: '.format(entrada), end='')
    entrada = int(input())
    palpite += 1

print('=' * 65)
print('\033[32mPARABÉNS!\033[m VOCÊ ACERTOU O NÚMERO QUE ESTAVA PENSANDO EM {} TENTATIVAS :)'.format(palpite))
