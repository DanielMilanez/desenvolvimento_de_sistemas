from os import system

def desenha(lista):
    system("clear")
    print("-------------")
    for i in range(len(lista)):
        print("|", end=' ')

        for j in range(len(lista[i])):
            print(lista[i][j], end=' | ')

        print()
        print("-------------")

def jogar(jogador, lista):
    if (jogador == 'X'):
        print("Primeiro jogador")
    else:
        print("Segundo jogador")

    linha = int(input("Informe uma linha >> "))
    coluna = int(input("Informe uma coluna >> "))

    lista[linha][coluna] = jogador
    