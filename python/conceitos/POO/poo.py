# PascalCase - primeira letra de todas as palavras maiuscula (apenas classe)
# camelCase - primeira letra começa minuscula mas as demais ficam maiúsculas

# Class - 'molde do objeto'

# __main__ arquivo atual
# __init__ instancia o objeto

class Motorista:
    # ... # Para que o python não reclame :P
    # def __init__() função construtor do objeto
    # self é um parametro padrão do python ele referencia a si mesmo

    # Toda classe pode ter um constructor
    def __init__(self, nome, carro, corCarro, placa):
        self.nome = nome 
        self.carro = carro 
        self.corCarro = corCarro
        self.placa = placa
    
    """
        Um construtor nada mais é do que uma função interna dentro de uma classe
        para que assim que um objeto for instanciado os atributos presentes na classe
        sejam atribuidos ao novo objeto gerado.
    """

# Objetos
motorista1 = Motorista('Geraldo', 'Renault Kwid', 'Preto', '3216-DFJ6')
motorista2 = Motorista('Robson', 'Fiat uno topo', 'Branco', '3216-GO03')
motorista3 = Motorista('Daniel', 'Koniggseg Agera', 'Laranja', '0905-MYPP')

# Escrevendo na tela
print(f'Informações sobre o motorista 1: \n Nome: {motorista1.nome} \n Carro: {motorista1.carro} \n Cor do carro: {motorista1.corCarro} \n Placa: {motorista1.placa} \n')
print(f'Informações sobre o motorista 2: \n Nome: {motorista2.nome} \n Carro: {motorista2.carro} \n Cor do carro: {motorista2.corCarro} \n Placa: {motorista2.placa} \n')
print(f'Informações sobre o motorista 2: \n Nome: {motorista3.nome} \n Carro: {motorista3.carro} \n Cor do carro: {motorista3.corCarro} \n Placa: {motorista3.placa} \n')
