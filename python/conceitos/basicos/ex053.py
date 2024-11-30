# Crie um programa que leia uma frase qualque e diga se ela é um palíndromo, desconsiderando os espaços

frase = input('Digite a frase: ').strip().lower()
frase = frase.replace(" ", "")

frase_invertida = frase[::-1]

if frase == frase_invertida:
    print('É um palindromo')
else:
    print('NÃO é um palindromo')
