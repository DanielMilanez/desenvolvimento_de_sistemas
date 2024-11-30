# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:

# ate 9 anos: mirim
# ate 14 anos: infantil
# ate 19 anos: junior
# ate 20 anos: senior
# acima: MASTER

from datetime import date
ano = date.today().year

nascimento = int(input('Digite a idade de nascimento do atleta: '))
idade = ano - nascimento

if idade <= 9:
    print('O atleta é mirim! pois possui {} anos'.format(idade))
elif 10 <= idade <= 14:
    print('O atleta é infantil! pois possui {} anos'.format(idade))
elif 15 <= idade <= 19:
    print('O atleta é junior! pois possui {} anos'.format(idade))
elif idade == 20:
    print('O atleta é sênior! pois possui {} anos'.format(idade))
else:
    print('O atleta é MASTER! pois possui {} anos'.format(idade))
