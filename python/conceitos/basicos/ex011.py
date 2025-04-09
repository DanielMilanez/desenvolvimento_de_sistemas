# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta - la, sabendo que cada litro de tinta, pinta uma área de 2m^2

print('='*30)
print('CALCULO DE TINTA')
print()

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
qnt_de_tinta = area / 2

print('\n Área total: {0} \n Quantidade de litros de tinta: {1}L'.format(area, qnt_de_tinta))
