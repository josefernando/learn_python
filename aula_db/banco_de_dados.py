import sqlite3

conexao = sqlite3.connect("aula.db")

def criar_tabela():
    conexao.execute(
        '''
create table if not exists aluno (
id integer primary key autoincrement,
nome text not null,
idade integer not null
);''')

    # print(f"Error: {conexao.Error}")

    conexao.commit()

def inserir_aluno(nome, idade):
    conexao.execute("insert into aluno (nome, idade) values (?,?);",(nome,idade))
    conexao.commit()

def listar_alunos():
    alunos = conexao.execute(
        '''
select * from aluno;
'''
    )
    for aluno in alunos:
        print(aluno)

def atualizar_aluno(id,nome,idade):
    conexao.execute("update aluno set idade=? where id=?;",(idade,id))
    conexao.commit()

def excluir_aluno(id):
    # ERROR: 'parameters are of unsupported type'
    # conexao.execute("delete from aluno where id = ?;",(id))
    #  ao passar apenas um valor inteiro.
    # solução:
    # envolva os argumentos com '[' ']'
    # conexao.execute("delete from aluno where id = ?;",[(id)])
    # ou coloque vírgula apois o argumento
    # conexao.execute("delete from aluno where id = ?;",(id,))

    conexao.execute("delete from aluno where id = ?;",(id,))

    conexao.commit()

# criar_tabela() 
inserir_aluno("Maria","21")
print("antes")
listar_alunos()
# atualizar_aluno(1,"manuel", 60)
print("depois")
excluir_aluno(4)
listar_alunos()