# Crie um programa que leia o nome completo de uma pessoa e mostre
# o nome com todas as letras maiúsculas
# o nomecom todas minúsculas
# quantas letras ao total sem considerar os espaços
# quantas letras tem o primeiro nome

name = input('Digite seu nome completo: ').strip()

print('MAIÚSCULO: {}'.format(name.upper()))
print('MINÚSCULO: {}'.format(name.lower()))

name = name.split()
letras = len(name[0])
name = ''.join(name)

print('Letras ao todo: {}'.format(len(name)))
print('Letras do primeiro nome: {}'.format(letras))
