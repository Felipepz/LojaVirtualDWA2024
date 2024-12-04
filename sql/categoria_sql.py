SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT
    );
"""

SQL_INSERIR = """
    INSERT INTO categorias(nome, descricao)
    VALUES (?, ?);
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, descricao
    FROM categorias
    ORDER BY nome;
"""

SQL_ALTERAR = """
    UPDATE categorias
    SET nome=?, descricao=?
    WHERE id=?;
"""

SQL_EXCLUIR = """
    DELETE FROM categorias
    WHERE id=?;
"""

SQL_OBTER_UM = """
    SELECT id, nome, descricao
    FROM categorias
    WHERE id=?;
"""
