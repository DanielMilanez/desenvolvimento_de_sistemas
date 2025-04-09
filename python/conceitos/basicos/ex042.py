# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado

# Equilatero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

side_a = float(input('Insira o valor do primeiro lado: '))
side_b = float(input('Insira o valor do primeiro lado: '))
side_c = float(input('Insira o valor do primeiro lado: '))

if side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b:
    print('É possivel formar um triângulo', end='')

    if side_a == side_b == side_c:
        print('EQUILATERO!')

    elif side_a == side_b or side_b == side_c or side_a == side_c:
        print('ISÓCELES!')

    else:
        print('ESCALENO!')

else:
    print('NÃO é possível formar um triângulo!')
