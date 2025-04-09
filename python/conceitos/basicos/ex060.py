# faça um programa que leia o número qualquer e mostre o seu fatorial

num = int(input('Digite um número para que eu possa ler o seu fatorial: '))

print('{}! = '.format(num), end='')
contador = num

while contador > 1:
    print('{} x '.format(contador), end='')
    num = num * (contador - 1)
    contador -= 1

print('1 >>> {}'.format(num))
