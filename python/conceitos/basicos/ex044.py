# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento

# a vista dinheiro/cheque: 10% de desconto
# a vista no credito: 5% de desconto
# em ate 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor_do_produto = float(input('Informe o preço do produto: R$ '))
forma_de_pagamento = input('Digite a forma de pagamento (dinheiro, cheque, credito ou a vista): ').strip().lower()

if 'dinheiro' in forma_de_pagamento or 'cheque' in forma_de_pagamento:
    value = valor_do_produto - (valor_do_produto * (10 / 100))
    print('Desconto de 10% aplicado!')
    print('O valor a ser pago será: R${:.2f}'.format(value))

elif 'a vista' in forma_de_pagamento:
    value = valor_do_produto - (valor_do_produto * (5 / 100))
    print('Desconto de 5% aplicado!')
    print('O valor a ser pago será: R${:.2f}'.format(value))

elif 'credito' in forma_de_pagamento:
    parcela = input('Deseja parcelar (sim / não)? ').strip().lower()

    if 'sim' in parcela:
        print('O valor do juros aplicado será de 20% para parcelas acima de 2x')
        vezes = int(input('Quantas vezes: '))

        if vezes <= 2:
            print('Preço normalizado do produto foi aplicado')
            print('Total a pagar: R${:.2f}'.format(valor_do_produto))

        else:
            valor_do_produto = valor_do_produto + ((valor_do_produto * (20 / 100)) * vezes)
            print('Preço atualizado, valor de 20% de juros aplicado')
            print('Total a pagar: {} parcelas de R${:.2f}'.format(vezes, valor_do_produto / vezes))

    elif 'não' in parcela:
        print('Preço normalizado do produto foi aplicado')
        print('Total a pagar: R${:.2f}'.format(valor_do_produto))

else:
    print('Forma de pagamento não reconhecida.')
