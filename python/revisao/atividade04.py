# To-do list
from os import system
lembrete = []
def lembretes():
    if not lembrete:
        print('Sem lembretes atuais.')
    else:
        print(f'Você possui {len(lembrete)} lembretes:')
        for i in range(len(lembrete)):
            print(f'{i + 1} - {lembrete[i]}')
    print('-' * 52)
    
    adicionar = input('Adicionar lembrete? (s/n) ').strip().lower()
    if adicionar == 's':
        lembrete_atual = input('Digite seu lembrete atual >> ')
        lembrete.append(lembrete_atual)
    else:
        return False 

while True:
    system('cls') 
    print('-' * 20, 'TO DO LIST', '-' * 20)
    confirm = lembretes()
    
    if confirm == False:
        break
