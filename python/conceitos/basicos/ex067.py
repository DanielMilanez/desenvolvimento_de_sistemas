# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# Quando o número solicitado for negativo, o programa será interrompido

num = 0
print('Digite um valor negativo para que o programa seja encerrado')
print('=' * 60)
while num > -1:
    num = int(input('Digite o número que deseja descobrir a tabuada: '))

    if num < 0:
        break

    print('~' * 30)
    for i in range(1, 11):
        print(f'{num} x {i:2} = {num * i}')

    print('~' * 30)
