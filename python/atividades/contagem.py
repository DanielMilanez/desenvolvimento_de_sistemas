# Calcular um algoritmo que conte de 1 a 100 e a cada multiplo de 10 exiba uma mensagem "Múltiplo de 10"

print("==" * 10, end=' ')
print("VERIFICANDO MÚLTIPLOS!", end=' ')
print("==" * 10)
print()
print("ao fim de uma linha o ultimo indice dela será um múltiplo de 10")
print()

for i in range(1, 101):
    print(i, end= ' ')
    if i % 10 == 0:
        print(">> É múltiplo de 10!")
        