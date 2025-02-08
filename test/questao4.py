class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.livros = []

    def adicionarLivros(self, *livros):
        for livro in livros: 
            self.livros.append(livro)  

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        autor.adicionarLivros(self)

new_autor = Autor('George Orwell', 'Britânico')

new_livro1 = Livro('A revolução dos bixos', 1945, new_autor)
new_livro2 = Livro('1984', 1949, new_autor)

print(f'Autor: {new_autor.nome} - {new_autor.nacionalidade}')
for livro in new_autor.livros:
    print(f'Título: {livro.titulo}, Ano: {livro.ano}')
