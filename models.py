class Autor:
    def __init__(self, nome, biografia, id):
        self.nome = nome
        self.biografia = biografia
        self.id = id

class livro:
    def __init__(self, titulo, ano, descricao, autor, genero, id):
        self.titulo = titulo
        self.ano = ano
        self.descricao = descricao
        self.autor = autor
        self.genero = genero
        self.id = id
        genero.adicionar_livros(self)
        
    def __str__(self):
        return f"{self.titulo} ({self.ano})"

    def __repr__(self):
        return self.__str__()

class Genero:
    def __init__(self, nome, id):
        self.nome = nome
        self.livros = []
        self.id = id

    def adicionar_livros(self, livro):
        self.livros.append(livro)
                    
