import calendar
from datetime import datetime
from os import system
from time import sleep

ano_autal = datetime.now().year
mes_atual = datetime.now().month
dia_atual = datetime.now().day

print(calendar.calendar(ano_autal))
while True:
    hora_atual = datetime.now().hour
    minutos_atuais = datetime.now().minute
    segundos_atuais = datetime.now().second
    
    sleep(1)
    system('cls')
    print(f'Você está no ano de {ano_autal} no mês {mes_atual} no dia {dia_atual}, na hora {hora_atual}:{minutos_atuais}:{segundos_atuais}')
