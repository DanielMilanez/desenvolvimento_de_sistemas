# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores

p_maiores = 0
p_menores = 0

for i in range(1, 8):
    idade = int(input('Digite a idade da {}° pessoa: '.format(i)))
    if idade >= 18:
        p_maiores += 1
    else:
        p_menores += 1

print('Atualmente existem {} pessoas maiores de idade e {} pessoas MENORES de idade'.format(p_maiores, p_menores))