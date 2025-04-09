import cria_cadastros as cc
import json
from os import system, path
dados_json = '.\python\\atividades\cadastro_login\dados.json'

system('cls')
if not path.exists(dados_json):
    cc.criar_cadastro(dados_json)

with open(dados_json, 'r', encoding='utf-8') as leitura:
    user = json.load(leitura)

def cadastro(login, senha):
    user['login'].append(login)
    user['senhas'].append(senha)

    with open(dados_json, 'w', encoding='utf-8') as leitura:
        json.dump(
            user,
            leitura
        )

def login(login, senha): 
    liberado = False
    for i in range(len(user['login'])):
        liberado = False

        login_existente = user['login'][i]
        senha_existente = user['senhas'][i]

        if login_existente == login and senha_existente == senha:
            liberado = True
            break
        else:
            continue
        
    print('Acesso liberado') if liberado == True else print('Acesso negado, usuário não existe')
    