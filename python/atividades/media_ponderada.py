# Calcular média de um aluno

def media():
    first = float(input('Informe a primeira nota >> ')) * 2
    second = float(input('Informe a primeira nota >> ')) * 3
    third = float(input('Informe a primeira nota >> ')) * 5
    return (first + second + third) / (2 + 3 + 5)

response = media()
print(f'A média do aluno é: {response:.2f}', end=' ')
print('\033[32mAPROVADO!\033[m' if response >= 5 else '\033[31mREPROVADO!\033[m')
