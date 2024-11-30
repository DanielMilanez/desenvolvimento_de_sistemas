# Desenvolva um programa que laia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres tem menos de 20 anos

soma_idade = 0
mais_velho = 0
sub_20 = 0
nome_mais_velho = ''

for i in range(1, 5):
    name = input('Digite o nome da {}° pessoa: '.format(i)).strip().capitalize()
    idade = int(input('Digite a idade de {}: '.format(name)))
    sexo = input('Digite o sexo de {} (M ou F): '.format(name)).strip().lower()
    print()

    soma_idade += idade
    if sexo == 'm':
        if mais_velho < idade:
            mais_velho = idade
            nome_mais_velho = name

    elif sexo == 'f' and idade < 20:
        sub_20 += 1

media = soma_idade / 4

print('A media de idade do grupo é {:.2f}'.format(media))
print('O nome do homem mais velho é {}'.format(nome_mais_velho))
print('Existem {} mulheres com menos de 20 anos no grupo'.format(sub_20))
