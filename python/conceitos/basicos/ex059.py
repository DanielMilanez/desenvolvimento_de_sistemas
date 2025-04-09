# crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# seu programa deverá realizar a operação solicitada em cada caso

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

print('=' * 50)
print('Digite uma opção \n [1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
print('=' * 50)

opt = int(input('Sua escolha: '))

while opt != 5:
    if opt == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
        print()

    elif opt == 2:
        print('{} X {} = {}'.format(num1, num2, num1 * num2))
        print()

    elif opt == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num1 < num2:
            print('{} é menor que {}'.format(num1, num2))
        else:
            print('{} é igual a {}'.format(num1, num2))

        print()

    elif opt == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))

        print()
    else:
        print('Entrada inválida. Tente novamente')

    print('=' * 50)
    print('Digite uma opção \n [1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa')
    opt = int(input('Sua escolha: '))
    print('=' * 50)
