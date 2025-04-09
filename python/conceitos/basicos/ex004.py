# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis

something = input('Digite qualquer coisa: ')

print('Algumas informações sobre o que você digitou')
print()
print('Tipo {0}, Alpha? {1}, AlphaNumber? {2}'.format(type(something), something.isalpha(), something.isalnum()))
