import sqlite3
import bcrypt


# Define o caminho do banco de dados
DB_PATH = "users.db"


def criar_conexao():
    """Cria conexão com o banco SQLite."""
    conn = sqlite3.connect(DB_PATH)
    return conn


def init_db():
    """Inicializa a tabela de usuários se não existir."""
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash BLOB NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def criar_usuario(username, password):
    """
    Cria um novo usuário.
    Returns:
        True se sucesso, False se o usuário já existir.
    """
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        bytes_senha = password.encode('utf-8')
        pwd_hash = bcrypt.hashpw(bytes_senha, bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                       (username, pwd_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Usuário já existe
    finally:
        conn.close()


def verificar_login(username, password):
    """Verifica a senha comparando o hash armazenado."""
    conn = criar_conexao()
    cursor = conn.cursor()
    # Busca o hash armazenado no banco
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        hash_armazenado = resultado[0]
        senha_fornecida = password.encode('utf-8')
        # O bcrypt verifica se a senha bate com o hash (magia segura)
        return bcrypt.checkpw(senha_fornecida, hash_armazenado)
    return False
