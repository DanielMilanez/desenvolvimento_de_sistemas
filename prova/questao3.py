from random import randint
from os import system

system('cls')
valor_gerado = randint(0, 100)
vidas = 5
print(valor_gerado)

print('==' * 10, 'ADIVINHE MEU NÚMERO SECRETO', '==' * 10)
print('Estou pensando em um número de 0 a 100, consegue adivinhar qual é?')

while True:
    tentativa = int(input('Seu palpite >> '))

    if tentativa > valor_gerado:
        print(f'OPS! O valor gerado é \033[33mMENOR\033[m do que o número {tentativa}')
    elif tentativa < valor_gerado:
        print(f'OPS! O valor gerado é \033[31mMAIOR\033[m do que o número {tentativa}')
    elif tentativa == valor_gerado:
        print(f'ISSO MESMO! \033[32mVOCÊ ACERTOU!\033[m MEU NÚMERO SECRETO É {valor_gerado}')
        break

    vidas -= 1

    if vidas == 0:
        print(f'Que pena... Você não conseguiu, o número que tinha pensado era: {valor_gerado}')
        print('Mais sorte na próxima.')
        break
