# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separados!

nome = input('Digite seu nome: ')
nome = nome.split()
primeiro_nome = nome[0]
ultimo_nome = nome[-1]

print('Seu primeiro nome é: {}'.format(primeiro_nome))
print('Seu último nome é: {}'.format(ultimo_nome))
