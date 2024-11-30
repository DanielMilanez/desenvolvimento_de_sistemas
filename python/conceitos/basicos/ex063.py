# Escreva um programa que leia um número X inteiro qualquer e mostre na tela os X primeiros elementos de uma
# sequencia de fibonacci

print('~' * 30)
num = int(input('Digite o número de casas a ser mostrado: '))
print('~' * 30)

first_value = 0
second_value = 1

# control
ctrl = 3

# Show the sequence
print(f'{first_value} > {second_value}', end='')

while ctrl <= num:
    plus_value = first_value + second_value
    print(f' > {plus_value}', end='')

    # loading new values
    first_value = second_value
    second_value = plus_value

    ctrl += 1

print(' > Fim da sequencia ')
print('~' * 30)
