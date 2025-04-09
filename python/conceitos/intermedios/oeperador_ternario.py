# Consigo fazer uma verificação boleana em apenas uma única linha

diga_ola = bool(input('Digite algo ou nada, mas aperte enter no final >> '))
print('Olá!') if diga_ola == True else print('Tchau!')
 