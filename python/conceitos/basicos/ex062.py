# Refazer desafio 61 mais perguntando quantos termos se deseja vizualizar ao digitar 0 o programa acaba

print('Lendo uma P.A. progreção aritmetica')
num = int(input('Digite o valor do primeiro termo desta PA: '))
raz = int(input('Agora, digite o valor da razão desta PA: '))

contador = 0

while contador < 10:
    print(num, end=' ')
    num += raz
    contador += 1

print()

terms = int(input('Quantos termos A MAIS você deseja ver? '))
contador_total = contador

while terms != 0:
    print(num, end=' ')
    num += raz
    contador += 1

    if contador >= terms:
        print()
        terms = int(input('Quantos termos A MAIS você deseja ver? '))
        contador = 0

print('fim do programa, foram exibidos {} termos'.format(contador_total))
