import sqlite3
import hashlib


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
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def hash_senha(senha):
    """Gera um hash SHA-256 da senha."""
    return hashlib.sha256(str.encode(senha)).hexdigest()


def criar_usuario(username, password):
    """
    Cria um novo usuário.
    Returns:
        True se sucesso, False se o usuário já existir.
    """
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        pwd_hash = hash_senha(password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                       (username, pwd_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Usuário já existe
    finally:
        conn.close()


def verificar_login(username, password):
    """
    Verifica se usuário e senha conferem.
    Returns:
        True se válido, False caso contrário.
    """
    conn = criar_conexao()
    cursor = conn.cursor()
    pwd_hash = hash_senha(password)
    cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?",
                   (username, pwd_hash))
    user = cursor.fetchone()
    conn.close()
    return user is not None
