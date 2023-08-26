import unittest
import sqlite3

from banco_de_dados import inserir_aluno, listar_alunos, atualizar_aluno, excluir_aluno

class TestCrud(unittest.TestCase):
    def setUp(self):
        self.conexao = sqlite3.connect(":memory:")
        self.conexao.execute(
            '''
    create table if not exists aluno (
    id integer primary key autoincrement,
    nome text not null,
    idade integer not null
    );'''
        )

    def tearDown(self):
        self.conexao.close()

    def test_inserir_aluno(self):
        inserir_aluno(self.conexao, "Roger", 25)
        inserir_aluno(self.conexao, "Manuela", 45)

        alunos = self.conexao.execute("SELECT * FROM aluno ORDER BY nome asc").fetchall()
        num_linhas = self.conexao.execute("SELECT count(*)").fetchall()

        print(num_linhas[0][0]) # numlinhas[primeira tupla][primeiro campo da tupla]

        self.assertEqual(len(alunos),2)
        self.assertEqual(alunos[0][1], "Manuela")

    def test_listar_alunos(self):
        inserir_aluno(self.conexao, "Roger", 60)
        inserir_aluno(self.conexao, "Manuela", 60)

        alunos = listar_alunos(self.conexao)

        alunosx = alunos.fetchall()
        self.assertEqual(len(alunosx),2)

    def test_atualizar_aluno(self):
        inserir_aluno(self.conexao, "Roger", 60)
        inserir_aluno(self.conexao, "Maria", 40)

        atualizar_aluno(self.conexao, 1 , "Roger", 65)

        aluno = self.conexao.execute("SELECT nome, idade FROM aluno").fetchall()
        idade00 = aluno[0][1]
        idade01 = aluno[1][1]

        self.assertEqual(idade00,65)
        self.assertEqual(idade01,40)

    def test_excluir_aluno(self):
        inserir_aluno(self.conexao, "Roger", 60)
        inserir_aluno(self.conexao, "Maria", 40)

        excluir_aluno(self.conexao, 2)

        aluno = self.conexao.execute("SELECT nome, idade FROM aluno").fetchall()

        self.assertEqual(len(aluno), 1)
        self.assertEqual(aluno[0][0], "Roger")