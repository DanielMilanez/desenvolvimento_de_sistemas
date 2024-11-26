# Conversor de moedas

value = float(input('Informe o valor que você possui >> R$'))

print('==' * 10, 'Conversões disponíveis', '==' * 10)
print('\n Dólares \n Ienes \n Euros')
opition = input('Informe qual das moedas você deseja converter >> ').strip().lower()

if opition == 'dolares':
    print(f'O valor convertido para dol é ${(value / 5.82):.2f}')
elif opition == 'ienes':
    print(f'O valor convertido para Iene é ¥{(value / 0.038):.2f}')
elif opition == 'Euros':
    print(f'O valor convertido para Euro é €{(value / 6.06):.2f}')

