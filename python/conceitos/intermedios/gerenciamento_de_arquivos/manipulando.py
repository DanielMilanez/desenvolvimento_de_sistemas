arquivo = '.\python\conceitos\intermedios\gerenciamento_de_arquivos\main.txt'
ascii_turtle = """
      ____     ____
    /      \  |  o | 
   |        |/ ___\| 
   |_________/     
   |_|_| |_|_|
"""

# MODOS

# a (append)
# w (escrita)
# r (read)
# x (criação)
# t (modo texto)
# w+, r+ (leitura, escrita)
# b (binário)

# leitura = open(arquivo, 'w')
# leitura.close()

# Dentro de um with
# write - escreve uma linha
# writelines - escreve multiplas linhas 
# seek - move cursor

with open(arquivo, 'w+') as leitura:
    leitura.write(ascii_turtle)
    leitura.seek(0, 0)
    print(leitura.read())
