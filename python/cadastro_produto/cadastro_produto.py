import cadastro_mod_produto as cmp

while True:
    cmp.exibir()
    confirm = input('Deseja cadastrar? ')

    if confirm == 's':
        nome = input('Informe o nome do produto >> ')
        price = float(input('Informe o preço do produto >> '))
        em_estoque = int(input('Informe a quantidade no estoque >> '))
        cmp.cadastro(nome, price, em_estoque)  
    
    else:
        break   

    cmp.exibir()
