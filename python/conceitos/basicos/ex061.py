# refaça o desafio 51 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# while

print('Lendo uma P.A. progreção aritmetica')
num = int(input('Digite o valor do primeiro termo desta PA: '))
raz = int(input('Agora, digite o valor da razão desta PA: '))

contador = 0

while contador < 10:
    print(num, end=' ')
    num += raz
    contador += 1
