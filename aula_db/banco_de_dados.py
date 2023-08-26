import sqlite3

conexao = sqlite3.connect("aula.db")

def criar_tabela(conexao):
    conexao.execute(
        '''
create table if not exists aluno (
id integer primary key autoincrement,
nome text not null,
idade integer not null
);''')

    # print(f"Error: {conexao.Error}")

    conexao.commit()

def inserir_aluno(conexao, nome, idade):
    conexao.execute("insert into aluno (nome, idade) values (?,?);",(nome,idade))
    conexao.commit()


def listar_alunos(conexao):
    alunos = conexao.execute(
        '''
select * from aluno;
'''
    )
    # for aluno in alunos:
    #     print(aluno)
    return alunos

def imprimir_alunos(conexao):
    alunos = listar_alunos(conexao)
    for aluno in alunos:
        print(aluno)
        print(f"Nome:  {aluno[1]}")
        print(f"Idade:  {aluno[2]}")

def atualizar_aluno(conexao, id, nome, idade):
    conexao.execute("update aluno set idade=? where id=?;",(idade,id))
    conexao.commit()

def excluir_aluno(conexao, id):
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

# criar_tabela(conexao) 
# print("antes")
# imprimir_alunos(conexao)
# inserir_aluno(conexao,"Maria","21")
# inserir_aluno(conexao,"Manuel","50")
# inserir_aluno(conexao,"Cláudio","35")
# print("depois")
# imprimir_alunos(conexao)
# # atualizar_aluno(conexao,3,"Maria", 65)
# #print("depois")
# # # excluir_aluno(4)
# # listar_alunos(conexao)
