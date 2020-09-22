import sqlite3

conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()


cursor.execute("""
SELECT * FROM cadastro;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
