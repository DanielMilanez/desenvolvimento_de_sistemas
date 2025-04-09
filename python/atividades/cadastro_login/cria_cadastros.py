import json

def criar_cadastro(dados_json):
    user = {
        'login': [],
        'senhas': []
    }
    with open(dados_json, 'a', encoding='utf-8') as leitura:
        json.dump(
                user,
                leitura
            )
