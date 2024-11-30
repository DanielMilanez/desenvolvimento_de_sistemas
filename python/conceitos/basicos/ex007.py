# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Insira a nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print('A média total é de: {:.3f}'.format(media))
