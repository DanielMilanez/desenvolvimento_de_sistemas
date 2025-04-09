# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# faça um programa que leia o nome dos quatro alunoes e mostre a ordem sorteada

import random

n1 = input('Digite 1° aluno: ')
n2 = input('Digite 2° aluno: ')
n3 = input('Digite 3° aluno: ')
n4 = input('Digite 4° aluno: ')

alunos = [n1, n2, n3, n4]
random.shuffle(alunos)

print('A ordem de apresentação será: {}'.format(alunos))
