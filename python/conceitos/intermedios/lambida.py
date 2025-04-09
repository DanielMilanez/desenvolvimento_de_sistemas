# ao trabalhar com uma função anonima, não precisamos chama-la, assim que executar o trecho a função será executada.

reais = float(input('Dolares que eu possuo >> '))
taxa = float(input('Informe o valor da taixa >> '))
converteDolar = lambda valor: valor / 6.66
converteIene = lambda valor, taxa: valor * 0.038 - taxa 

print(f'O valor convertido para Dolares é: {converteDolar(reais):.2f}')
print(f'O valor convertido para Ienes é: {converteIene(reais, taxa):.2f}')
