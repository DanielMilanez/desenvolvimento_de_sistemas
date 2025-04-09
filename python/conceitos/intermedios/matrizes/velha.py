import velha_dependences as td

lista = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

while(True):
    td.desenha(lista)
    td.jogar('X', lista)

    td.desenha(lista)
    td.jogar('O', lista)

    td.desenha(lista)
