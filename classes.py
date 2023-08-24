class Pessoa():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def saudacao(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos")

class Professor(Pessoa):
    def __init__(self, nome, idade, sexo, titulo):
        super().__init__(nome,idade,sexo)
        self.titulo = titulo

    def info(self):
        print(f"Meu título: {self.titulo}")     

pessoa1 = Pessoa("Rogéria",49,"M")         
pessoa2 = Pessoa("Manuel", 35, "Feminino")

pessoa1.saudacao()
Pessoa.saudacao(pessoa1)

prof1 = Professor("Francisca", 25, "F", "Doutor")

prof1.info();

prof1.saudacao();





