while True:
    try:
        peso = float(input('Digite seu peso: \n>> '))
        altura = float(input('Digite a sua altura: \n>>'))
        
        if peso and altura > 0: 
            IMC = peso / altura ** 2
            print(f'O seu IMC: {IMC:.2f}')
            break
        else:
            print(f'Valores de entrada não podem ser menores do que 0')
            continue
        
    except ZeroDivisionError as Error:
        print(f'{Error} \n Valores de entrada não podem ser 0')
        
    except ValueError as Error:
        print(f'{Error} \n Valores de entrada não podem ser letras, apenas números!')
