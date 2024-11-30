# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lidos

maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(i)))
    if peso >= maior_peso:
        maior_peso = peso
    elif menor_peso == 0 or peso <= menor_peso:
        menor_peso = peso

print('O maior é {}'.format(maior_peso))
print('O menor é {}'.format(menor_peso))
