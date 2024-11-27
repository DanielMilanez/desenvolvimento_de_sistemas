# Conversor de moedas

value = float(input('Informe o valor que você possui >> R$'))

print('==' * 10, 'Conversões disponíveis', '==' * 10)
print(' Dólares \n Ienes \n Euros')

dolar = lambda value: print(f'O valor convertido para Dolares é ${(value / 5.82):.2f}')
iene = lambda value: print(f'O valor convertido para Iene é ¥{(value / 0.038):.2f}')
euro = lambda value: print(f'O valor convertido para Euro é €{(value / 6.06):.2f}')

dolar(value) 
iene(value)
euro(value)

