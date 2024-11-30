# Refaça o desafio 09 mostrando a tabuada de um númeor que o usuário escolher, so que agora utlizando um laço for

print('TABUADA!!')
num = int(input('Digite um número: '))
print('A tabuada deste número é:')

for i in range(1, 11):
    print('{} X {:2} = {}'.format(num, i, num * i))
