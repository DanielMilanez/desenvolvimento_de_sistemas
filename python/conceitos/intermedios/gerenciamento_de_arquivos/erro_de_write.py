arquivo = '.\python\conceitos\intermedios\gerenciamento_de_arquivos\\teste.txt'

# Salvar um arquivo que contenha caracteres pode ocorrer um problema. Se possuir o padrão UTF-8 está tudo bem, caso contrário
# um problema será apresentado pelo programa ele não vai conseguir computar. Veja o exemplo.

# with open(arquivo, 'w+') as leitura:
#     leitura.write('APRESENTAÇÃO!!\n') # saida no arquivo: APRESENTA��O!!

# with open(arquivo, 'a', encoding='UTF8') as leitura:
#     leitura.write('ATENÇÃO!!') # saida no arquivo: ATENÇÃO!!

# Qualquer linguagem de programação lê arquivos Json
import json
dados = '.\python\conceitos\intermedios\gerenciamento_de_arquivos\\dados.json'

usuario = {
    'nome':'Emilia',
    'idade': 15,
    'cep': '2514-53'
}

with open(dados, 'w', encoding='utf-8') as leitura:
    # Armazena todos os indices e salva em um json
    json.dump(
        usuario,
        leitura,
        indent=2 # Indenta o código.
    )

with open(dados, 'r', encoding='utf-8') as leitura:
    pessoa = json.load(leitura)
    for chave, valor in pessoa.items():
        print(chave, valor)
