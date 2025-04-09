# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

dinheiro = float(input('R$: '))
cotacao = 3.27

print('$: {0:.2f}'.format(dinheiro / cotacao))
