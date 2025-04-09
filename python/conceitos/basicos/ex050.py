# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.

print('Somando números pares')
print('lembre-se que números impares são desconsiderados da soma')

total = 0
for i in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        total += num

print('O total da soma é: {}'.format(total))
