# Crie um programa que tenha uma tupla totalemtne preenchida com uma contagem por extenso, de zero ate vinte
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por exstenso.

numbers = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
    'treze', 'quatorze', 'quize', 'dezesses', 'dezesete', 'dezoito', 'dezenove', 'vinte'

num = int(input('Digite um número entre 0 e 20: '))

# Garantia de que o número seja de 0 a 20
while num > 20 or num < 0:
    num = int(input('\033[31mValor inválido.\033[0m Digite um número entre 0 e 20: '))

# Logica para converter número digitado para exstenso.
print(f'Você digitou o número \033[32m{numbers[num]}')
