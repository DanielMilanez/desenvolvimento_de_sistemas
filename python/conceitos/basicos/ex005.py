# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número: '))
sucessor = n1 + 1
antecessor = n1 - 1

print('O sucessor deste número é: {0} \n E o antecessor deste número é: {1}'.format(sucessor, antecessor))
