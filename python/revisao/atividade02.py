# Calcular conta

from os import system

system('cls')

print('Você e seus amigos sairam para comemorar um momento especial na vida de vocês.')
print('Todos escolheram ir em um restaurante. Sendo ele o mais chique da cidade.')
print('Diga-me quanto que vocês gastaram? ')
print()

print('--' * 10,'CALCULAR CONTA', '--' * 10)

pessoas = int(input('Quantas pessoas foram ao jantar >> '))
total_value = float(input('Total gasto >> '))

print(f'Cada pessoa do grupo teve que pagar R${(total_value / pessoas):.2f}')
print('-' * 56)
