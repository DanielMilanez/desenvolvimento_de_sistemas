"""
    Agregação ... Forma mia sespecializada de associação
"""

class Loja:
    def __init__(self):
        self.produtos = []
    
    # Adicionando o multiplicador conseguimos chamar mais de um termo ao mesmo tempo
    def addProdutos(self, *produto):
        for p in produto:  # Desempacotando os produtos para adicionar um por vez
            self.produtos.append(p)
    
    def listarProdutos(self):
        for produto in self.produtos:
            print(f'{produto.name} >> R${produto.price}')

class Produto:
    def __init__(self, name, price):
        self.name = name
        self.price = price

print('==' * 5, 'CASAS BAIBA', '==' * 5)
loja = Loja()
p1 = Produto('Ominitrix', 350)
p2 = Produto('HotWheels', 150)

loja.addProdutos(p1, p2)
loja.listarProdutos()
