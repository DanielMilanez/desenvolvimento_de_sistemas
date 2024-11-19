# Crie um programa que solicite ao usuário que insira 4 números. 
# Identifique e imprima o maior e o menor número da lista inserida.

numeros = []
for i in range(4):
    numero = int(input(f"Informe o {i + 1}° >> "))
    numeros.append(numero)
    
print(f'O maior e o menor valor são: {max(numeros)} || {min(numeros)}')
