# Calcular média de um aluno

def media():
    first = float(input('Informe a primeira nota >> ')) * 2
    second = float(input('Informe a primeira nota >> ')) * 3
    third = float(input('Informe a primeira nota >> ')) * 5
    return (first + second + third) / (2 + 3 + 5)

print(f'A média do aluno é: {media()}')
