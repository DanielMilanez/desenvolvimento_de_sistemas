# Utilizando dicionários

produto = {
    'nome': 'Leite',
    'price': 6.99,
    'em_estoque': 5
}

def mostrar():
    print("Produtos disponíveis")
    print(f'Nome do produto: {produto['nome']}')
    print(f'Preço unitário: {produto['price']}')
    print(f'No estoque há: {produto['em_estoque']}')
    print('==' * 10)

mostrar()

    