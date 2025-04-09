from os import system

system('cls')
estoque = {
    'itens': ['Cereal', 'Garrafa de água'],
    'qnt_itens': [10, 30]
}

def menu():
    print('==' * 10, 'CONTROLE DE ESTOQUE', '==' * 10)
    print('1 - para adicionar um novo produto no estoque')
    print('2 - para verificar um produto no estoque')
    print('3 - para atualizar um produto no estoque')

    opition = int(input('Digite a opção: ')) - 1

    match opition:
        case 0:
            exibir()
            itens = input('Informe o item a ser adicionado: ')
            qnt_itens = input('Informe a quantidade de itens disponíveis: ')
            adicionar(itens, qnt_itens)

        case 1:
            verificar()        
        
        case 2:
            atualizar()

def adicionar(itens, qnt_itens):
    estoque['itens'].append(itens)
    estoque['qnt_itens'].append(qnt_itens)

def verificar():
    count = 0
    for i in estoque['itens']:
        count += 1
        print(f'{count} - Itens: {i}')

    num_produto = int(input('Digite o número do produto a ser verificado >> ')) - 1
    verificado = int(estoque['qnt_itens'][num_produto])

    if verificado > 0:
        print(f'Produto está disponível: {verificado}')
    else:
        print(f'Produto está em falta: {verificado}')

def atualizar():
    count = 0
    for i in estoque['itens']:
        count += 1
        print(f'{count} - Itens: {i}')
    
    att = int(input('Informe o valor do indice a ser atualizado: ')) - 1
    estoque['qnt_itens'][att] = int(input('Informe a quantitade atualizada do produto >> '))

def exibir():
    print('Itens disponíveis!')
    for i in range(len(estoque['itens'])):
        print('---' * 10) 
        itens = estoque['itens'][i]
        qnt_itens = estoque['qnt_itens'][i]
        
        print(f'Itens: {itens}')
        print(f'Em estoque: {qnt_itens}')  
    print('---' * 10)    

for i in range(4):
    menu()
