# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um número qualquer: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print('O dobro de {0} é: {1} \n O triplo é: {2} \n E a raiz é de: {3:.3f}'.format(n1, dobro, triplo, raiz))
