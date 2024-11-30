# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco_produto = float(input('Insira o valor do produto: '))

desconto = preco_produto * (5 / 100)
val_final = preco_produto - desconto

print('Um produto com o valor de R${0} com o desconto de 5% ficará custando R${1:.2f}'.format(preco_produto, val_final))
