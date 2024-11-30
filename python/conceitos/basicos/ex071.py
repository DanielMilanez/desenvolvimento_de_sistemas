# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa informar quantas cédulas de cada valor serão entregues.

# OBS: considere que o caixa possui céculas de R$50, R$20, R$10 e R$1.
from os import system as sistema

sistema('cls')
print('=' * 30)
print(f'{'CAIXA DO MITCH':^30}')
print('=' * 30)

value = int(input('Por favor digite o valor a ser sacado: R$'))

montate = value
valor_v_atual = 50
valor_exibido = 0

print('~' * 30)

# looping para contagem de cedulas
while True:
    # Verificando se é possível subitrair o valor variavel atual do montante.
    if montate >= valor_v_atual:
        montate -= valor_v_atual
        valor_exibido += 1

    # Caso não seja, atualize o valor montate atual e imprima na tela quantas vezes ele foi usado.
    else:
        # Exibindo caso o valor seja diferente de 0
        if valor_exibido > 0:
            print(f'Total de {valor_exibido} cédulas de R${valor_v_atual}')

        # Alternando valores variáveis para quando o valor atual não puder mais ser usado
        if valor_v_atual == 50:
            valor_v_atual = 20

        elif valor_v_atual == 20:
            valor_v_atual = 10

        elif valor_v_atual == 10:
            valor_v_atual = 1

        # Fazendo com que o valor exibido retorne a 0 para que o proximo valor possa usar a contagem.
        valor_exibido = 0

        # Saindo do programa quando o montante total chegar a 0
        if montate == 0:
            break

print('~' * 30)
