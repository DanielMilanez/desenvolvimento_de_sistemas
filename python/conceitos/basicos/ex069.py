# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar ao
# usuário que ou não continuar. No final, mostre:

# A - Quantas pessoas tem mais de 18 anos
# B - Quantos homens foram cadastrados
# C - Quantas mulheres tem menos de 20 anos

contagem_maior = 0
homens_cadastrados = 0
sub_20 = 0

while True:
    print('-' * 40)
    print('CADASTRE UMA PESSOA')
    print('-' * 40)

    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo(M ou F): ').strip().lower()

    if idade > 18:
        contagem_maior += 1

    while sexo != 'm' and sexo != 'f':
        sexo = input('Digite o sexo(M ou F): ').strip().lower()

    if sexo == 'm':
        homens_cadastrados += 1

    elif sexo == 'f' and idade < 20:
        sub_20 += 1

    deseja_continuar = input('Deseja continuar (S/N)? ').strip().lower()

    while deseja_continuar != 's' and deseja_continuar != 'n':
        deseja_continuar = input('Deseja continuar (S/N)? ').strip().lower()

    if deseja_continuar == 'n':
        break

print('=' * 40)
print(f'Existem {contagem_maior} pessoas que possuem mais de 18 anos')
print(f'Existem {homens_cadastrados} homens cadastrados')
print(f'Existem {sub_20} mulheres com menos de 20 anos')
