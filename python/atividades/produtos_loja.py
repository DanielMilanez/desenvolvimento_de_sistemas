"""
    Duas lojas possuem estoques diferentes de produtos.
    Encontre os produtos disponíveis em ambas e os exclusivos de cada loja
"""
from os import system

system('cls')

primeira_l_produto = {'Macarrão', 'Molho de tomate', 'Banana', 'Leite', 'Peixe', 'Sabão em pó'}
segunda_l_produto = {'Macarrão', 'Suco', 'Refrigerante', 'Leite', 'Contra-filé', 'Sabão em pó'}

produtos_iguais = primeira_l_produto & segunda_l_produto
produtos_diferentes = primeira_l_produto ^ segunda_l_produto

print('Os produtos iguais das lojas são:', end=' ')
for produto in produtos_iguais:
    print(produto, end=' | ')
print()
print('==' * 40)

print('Os produtos diferentes em cada uma das lojas são:', end=' ')
for produto in produtos_diferentes:
    print(produto, end=' | ')
print()
print()