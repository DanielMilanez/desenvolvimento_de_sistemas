"""
    ENCAPSULAMENTO

    O python não possui modificador de acesso, ao invés disso ele utiliza convenções.
    - SEM UNDERLINE: PUBLIC
    - UMA UNDERLINE: PROTECTED (usado apenas dentro da classe)
    - DUAS UNDERLINE: PRIVATE (não é acessado por outras partes do código)
"""

class Carro:
    def __init__(self, modelo, cor, placa, peso, marca):
        self.__modelo = modelo
        self.cor = cor
        self._placa = placa
        self.peso = peso
        self. marca = marca
        self.km_atual = 0
    def alterarPlaca(self, placa):
        self.placa = placa
        print(f'Alterei a placa para {self.placa}')

carro_1 = Carro('Fiat Uno', 'Branco', 'FIATOP', 20, 'Fiat')
print(carro_1) # Retorna as informações de onde o objeto está salvo na memória.

# Métodos para acessar informações que estão dentro do objeto
print(vars(carro_1))
carro_1.alterarPlaca('ESCADAGOD')
print(carro_1.__dict__)
