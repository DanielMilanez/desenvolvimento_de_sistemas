# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele que ou não
# continuar a digitar os valores

cont = 's'
num = 0
maior = 0
menor = 0
soma = 0
contador = 0

while cont == 's':
    num = int(input('Digite um número: '))
    cont = input('Deseja continuar? (S/N): ').lower()

    if num > maior:
        maior = num
    if menor >= num or menor == 0:
        menor = num

    soma += num
    contador += 1

med_total = soma / contador

print('Valor total: {}'.format(soma))
print('A média de todos os valores digitados é: {}'.format(med_total))
print('O maior número digitado foi: {}'.format(maior))
print('O menor número digitado foi: {}'.format(menor))
