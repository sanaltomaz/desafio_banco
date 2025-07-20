#conector do servidor
import os 
import psycopg2
from dotenv import load_dotenv

load_dotenv()

database_URL = os.getenv("DATABASE_URL")

conn = None
cur = None

try:
    conn = psycopg2.connect(database_URL)
    print("Conexão com o banco de dados Neon estabelecida com sucesso!")
    nome = input("Digite o nome do cliente:")
    idade = int(input("Digite a idade do cliente:"))
    cpf = input("Digite o CPF do cliente:")
    email = input("Digite o email do cliente:")
    telefone = input("Digite o telefone do cliente:")

    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY, -- SERIAL é o tipo de auto-incremento no PostgreSQL
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf TEXT UNIQUE,
            email TEXT UNIQUE,
            telefone TEXT
        );
        """,
        
    )
    cur.execute(
         """
        INSERT INTO clientes(nome, idade, cpf, email, telefone)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;""",
        (nome, idade, cpf, email, telefone)
    )
    novo_id = cur.fetchone()[0]
    conn.commit()
    print("Dados inseridos com sucesso! ID do novo cliente:", novo_id)
except Exception as e:
    print(f"Erro: {e}")
    conn.rollback()
finally:
    if cur:
        cur.close()
    if conn: 
          conn.close()   



