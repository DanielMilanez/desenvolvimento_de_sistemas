# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seus status de acordo
# com a tabela abaixo

# abaixo de 18.5: Abaixo do peso
# entre 18.5 e 25: Peso ideal
# 25 ate 30: Obesidade
# acima de 40: obesidade mórbida

peso = float(input('Insira seu peso (Kg): '))
altura = float(input('Insira sua altura (Metros): '))

imc = peso / (pow(altura, 2))

if imc < 18.5:
    print('Abaixo do peso')

elif 18.5 <= imc < 25:
    print('Peso ideal')

elif 25 <= imc < 30:
    print('Obesidade')

elif imc >= 40:
    print('Obesidade morbida')

print('IMC = {}'.format(imc))
