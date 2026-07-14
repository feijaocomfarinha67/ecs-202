import sqlite3

print("Conectando ao banco de dados SQLite...")
# Cria o arquivo escola.db na mesma pasta onde o script rodar

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

# 1. TESTE DE DDL (Data Definition Language) - Criando a tabela
print("Criando a tabela de projetos...")

cursor.execute("""
CREATE TABLE IF NOT EXISTS projetos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tema TEXT NOT NULL,
    turma TEXT NOT NULL,
    nota REAL
)
""")

# Limpa a tabela para não duplicar se você rodar o script várias vezes
cursor.execute("DELETE FROM projetos")

# 2. TESTE DE DML (Data Manipulation Language) - Inserindo registros
print("Inserindo dados via SQL...")
cursor.execute("INSERT INTO projetos (tema, turma, nota) VALUES ('Projeto Integrador - Iniciação Científica', '301', 9.5)")
cursor.execute("INSERT INTO projetos (tema, turma, nota) VALUES ('Automação de Tarefas', '301', 10.0)")
cursor.execute("INSERT INTO projetos (tema, turma, nota) VALUES ('Aplicativo de Gestão', '201', 8.5)")

# Salva as alterações no banco
conexao.commit()

# 3. TESTE DE DQL (Data Query Language) - Consultando dados
print("\n--- RESULTADO DO SELECT (Apenas Turma 301) ---")
cursor.execute("SELECT id, tema, nota FROM projetos WHERE turma = '301' ORDER BY nota DESC")

# Captura todos os resultados encontrados pelo SQL
resultados = cursor.fetchall()

# Imprime os resultados no terminal do Python
for linha in resultados:
    print(f"ID: {linha[0]} | Tema: {linha[1]} | Nota: {linha[2]}")

print("\nFechando conexão...")
conexao.close()