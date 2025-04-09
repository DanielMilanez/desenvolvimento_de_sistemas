# UPER
class Cliente:
    def __init__(self, name, age, balance=0, avaliation=5):
        self.name = name
        self.age = age
        self.balance = balance
        self.avaliation = avaliation

    def addBalance(self, value):
        self.balance += value
        print(f'Saldo atual {value}')
    
    def removeBalance(self, value):
        self.balance -= value
        print(f'Saldo atual {value}')
    
    def avaliationEvent(self, value):
        while True:
            if value <= 5 and value >= 0:
                self.avaliation -= value
                break
            else:
                print('Valor inválido! Insira apenas valores de 0 a 5')
                value = int(input('Digite o valor da sua avaliação: '))

cliente = input('Informe seu nome: ')
age = int(input('Informe sua idade: '))
cliente = Cliente(cliente, age)

deposit = float(input('Digite o saldo para ser adicionado: '))
cliente.addBalance(deposit)

remove = float(input('Informe o valor da passagem: '))
cliente.removeBalance(remove)

print('==' * 20)
avaliation = int(input('Digite o valor da sua avaliação (0 / 5)'))
cliente.avaliationEvent(avaliation)

print('--' * 10, 'BEM VINDO A UPER', '--' * 10)
print(f'{"NOME":<20}{"SALDO":<10}{"AVALIAÇÃO":<10}') 
print(f'{cliente.name:<20}{cliente.balance:<10}{cliente.avaliation:<10}')
