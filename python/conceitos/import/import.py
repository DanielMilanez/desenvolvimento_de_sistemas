# import sys as sistema # puxa todas as funcionalidades
# from sys import exit as sair # puxa apenas uma única funcionaidade

# print(sistema.platform)
# print(sair())

from os import system as sistema
# sistema('shutdown /l') # Deslogar o usuário
sistema('rundll32.exe user32.dll,LockWorkStation')

"""
    para importar algo que eu programei eu utilizarei um módulo
    primeiro ciramos um arquivo e depois importamos ele, conseguimos
    acessar o que tem dentro do módulo clicando com botão esquerdo enquanto
    seguramos o ctrl
    
    O import de um módulo está limitado ao diretório que o arquivo está.
"""
from modulo_de_teste import somar
somar(num1=30, num2=10)

"""
    Quando criamos um modulo um arquivo chamado __pycache__ é criado no gitignore
    SEMPRE peça para ignorar este arquivo.
"""