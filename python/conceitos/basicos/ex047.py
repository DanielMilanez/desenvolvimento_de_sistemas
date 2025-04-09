# Desenvolva um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

print()
print('Mostrando \033[32mTODOS\033[0m os números pares entre 0 e 50 :)')
print('=' * 65)

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')

print()
print('=' * 65)
