# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER
# Exibindo no final o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

print('PAR OU IMPAR?')
print('~' * 30)

resp = input('digite sua resposta (PAR/IMPAR): ').strip().lower()
pontos = 0

if resp != 'par' and resp != 'impar':
    print('\033[31mEntrada inválida\033[0m, tente novamente. ')
    resp = input('digite sua resposta (PAR/IMPAR): ').strip().lower()

if resp == 'par':
    while True:
        escolha_pc = randint(0, 21)
        player_num = int(input('Seu número: '))

        result = escolha_pc + player_num

        print('IM', end='')
        sleep(0.5)
        print('PAR', end=' ')
        sleep(0.5)
        print('OU', end=' ')
        sleep(0.5)
        print('PAR')

        print(f'Eu escolhi: {escolha_pc}')
        print(f'O resultado é: {result}', end=' ')

        if result % 2 == 0:
            print('JOGADOR GANHOU!')
            pontos += 1
        else:
            break

if resp == 'impar':
    while True:
        escolha_pc = randint(0, 21)
        player_num = int(input('Seu número:  '))

        result = escolha_pc + player_num

        print('IM', end='')
        sleep(0.5)
        print('PAR', end=' ')
        sleep(0.5)
        print('OU', end=' ')
        sleep(0.5)
        print('PAR')

        print(f'Eu escolhi: {escolha_pc}')
        print(f'O resultado é: {result}', end=' ')

        if result % 2 != 0:
            print('JOGADOR GANHOU!')
            pontos += 1
        else:
            break

print()
print('~' * 30)
print('FIM DO JOGO!', end=' ')
print(f'Ao todo você marcou: {pontos}pts')
