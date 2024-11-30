# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
# o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print('-> Lembre-se que o valor do emprestimo não pode exceder 30% do seu salário <-')

casa = float(input('Informe o valor do imóvel: R$'))
salario = float(input('Digite seu salário: R$'))
anual = int(input('Agora digite em quantos anos você irá pagar: '))

minimo = salario * (30 / 100)
mensal = casa / (anual * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anual, mensal))

if mensal > minimo:
    print('\033[31mEmprestimo negado!\033[0m')
elif mensal <= minimo:
    print('\033[32mEmprestimo concedido!\033[0m')
