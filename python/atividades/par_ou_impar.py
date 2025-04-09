def verify(number):
    result = 'SIM' if number % 2 == 0 else 'NÃO'
    return result

number = int(input("Informe um valor para verificar se ele é par ou não >> "))
print(f'{number} é par? {verify(number)}')
