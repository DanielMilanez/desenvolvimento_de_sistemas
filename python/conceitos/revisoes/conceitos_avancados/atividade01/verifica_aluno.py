# Verificar se existem alunos já existentes, e salvando dados atuais em um json
import time
import json
import main
from os import path
from os import system

def existence(link_arquivo):
    global dados
    system('cls')

    if not path.exists(link_arquivo):
        print('\033[31mArquivo alunos não existe.\033[m Criando arquivo...')
        
        alunos = {'aluno': [], 'nota': [], 'media': []}
        
        with open(link_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(alunos, arquivo, indent=2)

    print('\033[32mCarregando dados', end='', flush=True)
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(0.5) 

    with open(link_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        
    time.sleep(1)  
    print('\033[33m Dados carregados!\033[m')

def cadastro(link_arquivo):
    aluno = input('Informe o nome do aluno >> ')
    alunos = []

    dados['aluno'] = alunos.append(aluno)
    notas = []
    while True:
        try:
            insert_notas = int(input('Informe quantas avaliações foram aplicadas >> '))
            for i in range(insert_notas):
                nota = float(input(f'Informe a {i + 1}° nota do aluno: '))
                notas.append(nota) 

            dados['nota'] = notas
            break
        except:
            print('Valores inválidos, por favor insira valores adequados.')

    media = main.Aluno.adicionarNota(notas)
    # Cadastrando dados no arquivo json
    with open(link_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2)

    return aluno, notas
