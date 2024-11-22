produto = {
    'nome': ['Pastel', 'Leite'],
    'price': [6.99, 4.99],
    'em_estoque': [5, 10]
}

def exibir():
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

exibir()

nome = input('Informe o nome do produto >> ')
price = float(input('Informe o preço do produto >> '))
em_estoque = int(input('Informe a quantidade no estoque >> '))

produto['nome'].append(nome)
produto['price'].append(price)
produto['em_estoque'].append(em_estoque)

exibir()
