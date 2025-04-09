from os import system as sy

produto = {
    'nome': ['Pastel', 'Leite'],
    'price': [6.99, 4.99],
    'em_estoque': [5, 10]
}

def cadastro(nome, price, qnt_estoque):
    produto['nome'].append(nome)
    produto['price'].append(price)
    produto['em_estoque'].append(qnt_estoque)

def exibir():
    sy('cls')
    # Exibir produtos!
    for i in range(len(produto['nome'])):
        print('---' * 10) 
        nome = produto['nome'][i]
        price = produto['price'][i]
        em_estoque = produto['em_estoque'][i]
        
        print(f'Produto: {nome}')
        print(f'Preço: {price}')
        print(f'Em estoque: {em_estoque}')  
    print('---' * 10)    
