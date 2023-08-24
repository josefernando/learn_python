class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def toString(self):
        print(f"titulo: {self.titulo}, autor: self.autor")

livro1 = Livro("Capitães de areia", "Jorge Amado")

livro1.toString();

