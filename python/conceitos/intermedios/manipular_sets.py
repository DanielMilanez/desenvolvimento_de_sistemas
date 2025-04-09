"""
    1° NÃO TEM INDICE (NÃO GARANTE ORDEM)
    2° NÃO ACEITAM CONTEÚDOS REPETIDOS!
"""

from os import system as sy
sy('cls')

# CRIANDO UM SET
print('--' * 10, 'CRIANDO UM SET', '--' * 10)
a = set('DANIEL') # a = {'DANIEL'} também pode ser utilziado
print(a)

teste = ['oi', 'oi', 'oi']
# Irá juntar os elementos repetidos e apenas exibirá um único elemento que representa todos os outros
print(set(teste)) 

b = {1, 2, 3, 4, 5, 6, 'DANIEL'}
print(b)

c = set() # Ao usar {} será considerado um dicionário
print(c, type(c))

# METODOS UTEIS
print('--' * 10, 'METODOS UTEIS', '--' * 10)

conjunto = set()
print(conjunto)

conjunto.add(10) # Adcionando valor
conjunto.add(8) # Adcionando valor

print(conjunto)

conjunto.update((3, 5, 6, 'BOM DIA')) # Atualizando conjunto
print(conjunto)

""" 
    Removendo o valor do conjunto, ele não trabalha com indice, e irá remover o
    primeiro conteudo que atende o parametro
"""
conjunto.discard('BOM DIA') 
print(conjunto)

# OUTRAS CARACTERISTCAS
print('--' * 10, 'OUTRAS CARACTERISTCAS', '--' * 10)

conjuntoA = {1, 2, 3, 4, 5}
conjuntoB = {5, 6, 7, 8, 9}
conjuntoC = set()

print(conjuntoA)
print(conjuntoB)
print(conjuntoC)

print('-' * 50)

# UNIÃO (union)
print('União entre A e B', end=' ')
conjuntoC = conjuntoA.union(conjuntoB) # podemos utilizar o | para realizar a união
print(conjuntoC)

# INTERSECÇÃO (intersection)
print('Valor em comum entre A e B', end=' ')
conjuntoC = conjuntoA.intersection(conjuntoB) # podemos utilizar o & para realizar o intersection
print(conjuntoC)

# DIFERENÇA
print('Diferença do conjunto A para o B', end=' ')
conjuntoC = conjuntoA.difference(conjuntoB) # podemos utilizar o - para o conjunto da esquerda
print(conjuntoC)

print('Diferença do conjunto B para o A', end=' ')
conjuntoC = conjuntoB.difference(conjuntoA) # podemos utilizar o ^ para todos os dois conjuntos
print(conjuntoC)
