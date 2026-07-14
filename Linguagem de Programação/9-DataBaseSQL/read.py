import sqlite3

print("--- RANKING OFICIAL ---")

# 1. Conecta ao arquivo do banco de dados que já existe
con = sqlite3.connect("jogadores.db")
cursor = con.cursor()

# 2. Executa a busca (SELECT) ordenando do maior para o menor (DESC)
cursor.execute("SELECT nick, pontos FROM ranking ORDER BY pontos DESC")

# 3. Pega todos os resultados e guarda na variável 'jogadores'
jogadores = cursor.fetchall()

# 4. Usa o laço for para percorrer a lista e mostrar na tela
for linha in jogadores:
    # linha[0] é o nick, linha[1] são os pontos
    print(f"Jogador: {linha[0]} | Pontuação: {linha[1]}")

# 5. Fecha a conexão com o arquivo
con.close()

print("-----------------------")