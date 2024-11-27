from os import system
lembrete = []

def lembretes():
    if not lembrete:
        print('Sem lembretes atuais.')
        
    else:
        system('cls')
        print(f'Você possui {len(lembrete)} lembretes:')
        for i in range(len(lembrete)):
            print(f'{i + 1} - {lembrete[i]}')
            
    print('-' * 52)
    
    new_opit = input('Adicionar lembrete s/n? (r para remover) ').strip().lower()
    if new_opit == 's':
        lembrete_atual = input('Digite seu lembrete atual >> ')
        lembrete.append(lembrete_atual)
    
    elif new_opit == 'r':
        if not lembrete:
            return 'vazio'
        else:
            removing = int(input('Insira a opção do lembrete para remover >> ')) 
            lembrete.pop(removing - 1)
    else:
        return False 

while True:
    print('-' * 20, 'TO DO LIST', '-' * 20)
    confirm = lembretes()
    
    if confirm == False:
        break
    elif confirm == 'vazio':
        system('cls')
        print('Não é possível remover um item de uma lista vazia.')
