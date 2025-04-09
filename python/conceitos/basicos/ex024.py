# Cria um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome_cidade = input('Digite o nome de sua cidade: ').strip()

santo = nome_cidade.upper().startswith('SANTO')

print('A cidade começa com "SANTO"? {}'.format(santo))
