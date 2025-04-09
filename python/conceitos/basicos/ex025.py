# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input('Digite seu nome: ')
nome = nome.upper()
print('Seu nome possui Silva? {}'.format('SILVA' in nome))
