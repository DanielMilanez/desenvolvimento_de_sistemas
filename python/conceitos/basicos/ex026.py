# faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra "A"
# em qual posição ela aparece a primeira vez
# em qual posição ela aparece a última vez

frase = input('Digite uma frase: ').strip()

frase = frase.upper()
print('Quantas vezes aparece a letra "A"? {}'.format(frase.count('A')))
print('Em qual posição aparece a letra "A" pela primeira vez? {}'.format(frase.find('A') + 1))
print('Em qual posição ela aparece pela ÚLTIMA vez? {}'.format(frase.rfind('A') + 1))
