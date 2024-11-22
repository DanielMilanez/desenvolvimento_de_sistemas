# Armazenar número de telefone

agenda = {
    'describe': None
}

while True:
    try:
        confirm = input('Deseja cadastrar um novo contato? (s/n)? ').strip().lower()
        
        if confirm != 'n' and confirm != 's':
            print('\033[31mEntrada inválida\033[m, digite s ou n')
        elif confirm == 'n' or confirm != 's':
            break
        elif confirm == 's':
            nome = input('Contato >> ')
            telefone = int(input(f'Número de {nome} >> '))
            tag = input('Descrição >> ')
            print('*' * 30)
            
            agenda.update({
                'describe' : tag 
            })
            
            agenda.update({
                nome : telefone
            }) 
    except:
        print('\033[31mEntrada inválida\033[m, digite s ou n')

print('=' * 30, 'AGENDA ELETÔNICA', '=' * 30)
for contato in agenda.items():
    print(f'📧 Nome {contato[0]}')
    print(f'Telefone 📞 {contato['nome']}')
    print(f'{agenda['describe']}')
