# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade

# se ele ainda vai se alistar ao serviço militar.
# se é a hora de se alistar
# se ja passou do tempo do alistamento

# seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

nascimento = int(input('Digite o ano em que você nasceu: '))
ano = date.today().year

idade = ano - nascimento

if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    anos = 18 - idade
    print('Faltam {} ano(s) para você se alistar'.format(anos))
else:
    anos = idade - 18
    print('Já se passaram {} ano(s), desde o seu alistamento'.format(anos))
