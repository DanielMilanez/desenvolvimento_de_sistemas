# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
# de acordo com a média atingida:

# Média abaixo de 5: REPROVADO
# Média entre 5 e 6.9: RECUPERAÇÃO
# Média 7 ou superior: APROVADO

nota1 = float(input('Informe a nota do aluno: '))
nota2 = float(input('Informe a nota do aluno: '))

media = nota1 + nota2 / 2

if media < 5.0:
    print('Aluno REPROVADO! nota total {}'.format(media))
elif 5.0 < media < 6.9:
    print('Aluno em RECUPERAÇÃO! nota total {}'.format(media))
elif media >= 7.0:
    print('APROVADO! nota total {}'.format(media))
