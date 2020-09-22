import sqlite3
conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE cadastro (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nomeCompleto TEXT NOT NULL,
        idade INTERGER,
        cpf VARCHAR(11) NOT NULL,
        logradouro TEXT NOT NULL,
        numero INTERGER NOT NULL,
        complemento TEXT,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado VARCHAR (2) NOT NULL,
        renda FLOAT NOT NULL,
        score INTERGER NOT NULL,
        limite TEXT NOT NULL
);
""")

conn.close()
