"""
    RELAÇÕES ENTRE CLASSES
    - Associação ... Relaciona um objeto a outro.  
"""

# Asmazon
class User:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self._password = password
        self.book = None

# -------------------- ACESSANDO O LIVRO ---------------------------
    @property # Chamando o objeto externo e retornando
    def bookAdd(self): 
        return self.book
    
    # Pega o que foi retornando e acrecenta na variável livro.
    @bookAdd.setter # Realiza a Associação de um objeto em outro
    def adicionarLivro(self, bookAdd):
        self.book = bookAdd
# ------------------------------------------------------------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def mostrarAutor(self):
        return self.author


new_user = User('Daniel', 'danielmilanez', 'S3nh4')
new_book = Book('1984', 'George Orwel')

new_user.book = new_book
print(new_user.book.mostrarAutor())

print(f'INFORMAÇÕES DA CONTA \n USER >> {new_user.__dict__} \n LIVRO >> {new_book.__dict__}')
print(f'{new_user.book}')
