alunos = {
    'nome': 'Daniel',
    'idade': 15,
    'nota': [3.6, 7.6, 9, 7.6]
}
try:
    selecao = input('O que você deseja selecionar> \n >> ')
    print(f'{alunos[selecao]}')
    
except KeyError as Error:
    print(f'Este campo >> {Error}<< não existe. \n Aqui está a lista dos campos esistentes: \n {tuple(alunos.keys())}')
    