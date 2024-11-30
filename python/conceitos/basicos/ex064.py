# Crie um programa que leia vários números inteiros pleo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)

stop_cond = 0
contador = 0
total = 0

while stop_cond != 999:
    num = int(input('Digite um número [999 para parar]: '))

    if num != 999:
        contador += 1
        total += num
    stop_cond = num

print('Ao todo foram digitados {} números, e a soma total entre eles é de: {}'.format(contador, total))
