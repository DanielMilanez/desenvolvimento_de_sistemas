# Exibir o maior valor dentre todos!

print("==" * 10, end=' ')
print("EXIBIR O MAIOR VALOR", end=' ')
print("==" * 10)
print()

maior = 0 
for i in range(3):
    numero = int(input("Digite o número >> "))
    if maior < numero:
        maior = numero

print(f"O maior valor lido é: {maior}")
