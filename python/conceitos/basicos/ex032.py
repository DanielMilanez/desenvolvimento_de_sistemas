# Desenvolva um programa que consiga dizer se o ano é bissexto ou não

from datetime import date

ano = int(input('Digite o ano (digite 0 para usar o ano atual): '))

if ano == 0:
    ano = date.today().year

result = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

if result:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))

# um ano so pode ser bissexto s ele for divisível por 4 e ele apenas poderá ser quando for divisivel por 100 se ao mesmo
# tempo for divisivel por 400, caso contrário ele não é bissexto.
