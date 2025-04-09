# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado!


km = float(input('Informe a quantidade de Km percorridos: '))
dias = int(input('Agora, informe a quantidade de dias: '))

valor_pago = (dias * 60) + (km * 0.15)

print('Ao fim do dia você deverá pagar {:.2f} do valor rodado'.format(valor_pago))
