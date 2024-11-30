# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três que
# se encontram no intervalo de 1 até 500

print('CALCULANDO a soma de números divisiveis por 3 entre 1 e 500')

# variável contadora!
num = 0
print('São os múltiplos: ', end=' ')
for i in range(1, 500):
    if i % 2 != 0:
        if i % 3 == 0:
            num += i
            print(i, end=' ')
print()
print('A somatória total dos multiplos é: {}'.format(num))
