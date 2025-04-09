# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo

lado_a = float(input('Insira o valor do primeiro lado: '))
lado_b = float(input('Insira o valor do primeiro lado: '))
lado_c = float(input('Insira o valor do primeiro lado: '))

if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_a + lado_c > lado_b:
    print('PODE FORMAR um triângulo!')
else:
    print('NÃO PODE formar um triângulo!')
