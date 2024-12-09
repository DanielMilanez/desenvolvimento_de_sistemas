from os import system

# Conversor de moedas
dolar = lambda value: print(f'O valor convertido para Dolares é ${(value / 5.82):.2f}')
iene = lambda value: print(f'O valor convertido para Iene é ¥{(value / 0.038):.2f}')
euro = lambda value: print(f'O valor convertido para Euro é €{(value / 6.06):.2f}')

value = float(input('Informe o valor que você possui >> R$'))
system('cls')
while True:
    print(f'Valor a ser convertido >> {value}')
    try:
        print('==' * 10, 'Conversões disponíveis', '==' * 10)
        print(' Dólares \n Ienes \n Euros') 
        
        opition = input('Informe a operação >> ').strip().capitalize()

        if opition == 'Dólares' or opition == 'Dolares':
            dolar(value)
            break
            
        elif opition == 'Ienes' or opition == 'Iene':
            iene(value)
            break
            
        elif opition == 'Euros' or opition == 'Euro':
            euro(value)
            break
        
        else:
            system('cls')
            print('Entrada inválida, insira valores adequados!')
            
    except Exception as Error:
        system('cls')
        print(f'Um erro inesperado ocorreu! {Error}')
