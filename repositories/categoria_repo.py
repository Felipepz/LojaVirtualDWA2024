from models.categoria_model import Categoria
from sql.categoria_sql import *
from util.database import obter_conexao
import sqlite3
from typing import List, Optional

class CategoriaRepo:
    @classmethod
    def criar_tabela(cls):
        """Cria a tabela de categorias no banco de dados."""
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls, categoria: Categoria) -> Optional[Categoria]:
        """Insere uma nova categoria no banco de dados."""
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR,
                    (categoria.nome, categoria.descricao)
                )
                if cursor.rowcount > 0:
                    categoria.id = cursor.lastrowid
                    return categoria
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_todos(cls) -> List[Categoria]:
        """Retorna todas as categorias."""
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS).fetchall()
                categorias = [Categoria(*t) for t in tuplas]
                return categorias
        except sqlite3.Error as ex:
            print(ex)
            return []

    @classmethod
    def alterar(cls, categoria: Categoria) -> bool:
        """Atualiza uma categoria existente no banco de dados."""
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR,
                    (categoria.nome, categoria.descricao, categoria.id)
                )
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def excluir(cls, id: int) -> bool:
        """Exclui uma categoria pelo ID."""
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_EXCLUIR, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_um(cls, id: int) -> Optional[Categoria]:
        """Retorna uma única categoria pelo ID."""
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_UM, (id,)).fetchone()
                if tupla:
                    return Categoria(*tupla)
                return None
        except sqlite3.Error as ex:
            print(ex)
            return None
