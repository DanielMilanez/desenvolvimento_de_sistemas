# Crie um programa que cadastre alunos em um sistema utilizando POO, os alunos cadastrados devem ter seus dados salvos em um arquivo json
import verifica_aluno as va
link_arquivo = '.\python\conceitos\\revisoes\conceitos_avancados\\atividade01\\aluno_dados.json'

va.existence(link_arquivo)

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self._notas = []

    def adicionarNota(self, *nota):
        for n in nota:  
            self._notas.append(n)
    
    def calcularMedia(self):
        if self._notas:
            return sum(self._notas / len(self._notas))     
        else:
            print('Notas não cadastradas.')
            return 0
        
    def aprovado(self):
        media = self.calcularMedia()
        
        if media >= 7:
            print(f'Aluno \033[32m{self.nome}\033[m foi \033[32mAprovado\033[m {media:.2f}')

        elif media >= 5:
            print(f'Aluno \033[32m{self.nome}\033[m ficará de \033[33mRecuperação\033[m {media:.2f}')

        else:
            print(f'Aluno \033[32m{self.nome}\033[m foi \033[31mReprovado\033[m {media:.2f}')

aluno = va.cadastro(link_arquivo)
Aluno(aluno)
