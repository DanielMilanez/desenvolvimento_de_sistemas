# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntas se o usuário vai continuar
# No final, mostre:

# Total gasto na compra
# Quantos produtos custam mais de R$1000
# Qual é o noem do produto mais BARATO

total_value = 0
cheap_item = ''
cheap_item_value = 0
count_item = 0

print('=' * 40)
print('Cadastre um produto :)')
print('=' * 40)

while True:
    name = input('Digite o nome do produto: ').strip().capitalize()
    price = float(input('Digite o preço do produto: R$'))

    deseja_continuar = input('Deseja continuar (S/N)? ').strip().lower()

    total_value += price

    if cheap_item_value == 0 or price < cheap_item_value:
        cheap_item_value = price
        cheap_item = name

    if price > 1000:
        count_item += 1

    while deseja_continuar not in ['s', 'n']:
        deseja_continuar = input('Deseja continuar (S/N)? ').strip().lower()

    if deseja_continuar == 'n':
        break

print('=' * 40)
print(f'O valor total gasto na compra é R${total_value:.2f}')
print(f'Existem {count_item} produtos custando mais de R$1000.00')
print(f'O nome do produto mais barato é: {cheap_item} custando R${cheap_item_value:.2f}')
