# Escreva um programa que leia a velocidade de um carro se ele ultrapassar 80 mostre uma mensagem dizendo que ele
# foi multado no valor de 7 reais por cada km acima da velocidade

km = float(input('Insira a kilometragem: '))

if km > 80:
    print('Velocidade ultrapassou o limite permitido, aplicando multa')
    valor = km - 80
    print('O valor a pagar é: R${}'.format(valor * 7))
else:
    print('Carro não ultrapassou o limite, sem multa aplicada :)')
