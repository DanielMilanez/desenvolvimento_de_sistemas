# Desenvolva um programa que pergunte a distância de uma viagem, em km. Calcule o preço da passagem custando
# 0.50 por km para viajens acima de 200km e 0.45 para viajes mais longas

km = int(input('Insira a distância da viajem: '))

if km <= 200:
    valor = km * 0.50
    print('O valor total da viajem é R${}'.format(valor))
else:
    valor = km * 0.45
    print('O valor total da viajem ficou R${}'.format(valor))

