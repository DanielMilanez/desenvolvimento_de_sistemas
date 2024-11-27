"""
    Faça um algoritmo que avalie se o usuario e senha cadastrados e 
    se não tiver, printe uma falha
    senao printe que deu tudo certo
"""

import getpass

print('==' * 10, 'LOGIN', '==' * 10)
login = input('Login >> ')
senha = getpass.getpass('Senha >> ')

print('Acesso liberado') if senha == 'ADM' and login == 'ADM' else print('Acesso negado!')

print('=' * 47)
