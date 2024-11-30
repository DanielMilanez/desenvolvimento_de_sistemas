# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Insira a distancia: '))

centrimetros = metros * 100
milimetros = metros * 1000

print('\n Metros: {0:.2f}m \n Centimetros: {1:.2f}cm \n Milimetros: {2:.2f}mm'.format(metros, centrimetros, milimetros))
