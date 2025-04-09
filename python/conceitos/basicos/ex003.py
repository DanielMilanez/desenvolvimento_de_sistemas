# fazer a soma de dois valores inseridos pelo usuário, no python a função input retorna um valor do tipo string
# então o que precisamos faze é converter o valor de string para inteiro, e em seguida fazer a soma dos dois números
# para fazer isso eu preciso informar ao interpretador que o tipo primitivo que eu desejo é inteiro e para isso uso
# a função int!

num_01 = int(input('Digite um número: '))
num_02 = int(input('Digite um segundo número:'))
s = num_01 + num_02

print('A soma total entre {0} e {1} é de: {2}'.format(num_01, num_02, s))
