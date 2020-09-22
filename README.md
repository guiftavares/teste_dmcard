# GYPZ - Teste de Desenvolvedor

Aplicação desenvolvida em Python 3.8 e banco de dados Sql.

# BANCO DE DADOS

Banco de Dados criado utilizando SQLite no Python 3.8
Tabela:

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


# FUNÇÃO PARA OBTENÇÃO DO SCORE

import random

def pontuacao():
    for x in range(1):
        pontuacao = random.randint(1,999)
        return pontuacao
