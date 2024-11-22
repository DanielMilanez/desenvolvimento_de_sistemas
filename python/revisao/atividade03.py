from os import system as sy

selections = []
produtos = [
    ['Leite', 6.99],
    ['Manteiga', 7.99],
    ['Picanha', 29.99],
    ['Batata', 3.99],
    ['Molho de tomate', 2.99]
]

sy('cls')
print('Em casa, você percebe que há itens que estão faltando para a festa que você irá fazer.')
print('Você precisa ir ao mercado para poder repor os itens.')
print()

print('--' * 10, 'SUPER MEIA BOCA', '--' * 10)

for item in range(len(produtos)):
    print(f'{item + 1} -  {produtos[item][0]} -- R${produtos[item][1]:.2f}')    
print('-' * 57)

while True:
    opition = int(input('Selecione o índice do item desejado (ou -1 para finalizar) >> '))
    if opition == -1:
        break
    if 1 <= opition <= len(produtos): 
        selections.append(opition - 1)
    else:
        print("Opção inválida! Por favor, escolha um número válido.")

total = 0
for i in selections:
    total += produtos[i][1] 

print(f'Valor total >> R${total:.2f}')
