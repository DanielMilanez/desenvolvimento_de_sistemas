# Ordenando uma lista em ordem númerica

conjunto = [5, 8, 2, 9, 1]
print(conjunto)

conjunto.sort()
# Ordem crescente
print(conjunto)

# Ordem decrecente
conjunto.sort(reverse=True)
print(conjunto)

# Adicionando valor 7 ao fim da lista
conjunto.append(7)
print(conjunto)

# Adicionando na posição 2 o valor 3
conjunto.insert(2, 3)
print(conjunto)

# Trocando o valor da posição 1 por 10
conjunto[1] = 10
print(conjunto)

# Removendo o valor 9 da lista
conjunto.remove(9)
print(conjunto)

# Excluindo elemento da posição 2 ate a 4 (incluindo a 4)
del conjunto[2:5]
