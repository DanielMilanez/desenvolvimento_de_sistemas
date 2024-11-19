# Demonstrar para o usuário a tabuada de um determinado número

print("==" * 10, end=' ')
print("CALCULANDO A TABUADA", end=' ')
print("==" * 10)
print()

num = int(input("Informe o número >> "))

for i in range(10):
    print(f"{num:2} X {i + 1:2} = {(i + 1) * num:2}")

print("==" * 30)
