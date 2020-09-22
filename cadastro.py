from datetime import datetime
import sqlite3
import random
import score


conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()


p_nomeCompleto = str(input('Nome Completo: '))
p_idade = int(input('Idade: '))
p_cpf = int(input('CPF: '))
p_logradouro = str(input('Logradouro: '))
p_numero = int(input('Número: '))
p_complemento = str(input('Complemento: '))
p_bairro = str(input('Bairro: '))
p_cidade = str(input('Cidade: '))
p_estado = str(input('UF: '))
p_renda = float(input('Renda (R$): '))
p_score = score.pontuacao()

if p_score > 950:
    p_limite = 1000000
else:
    if(p_score >= 800) and (p_score <=950):
         p_limite = p_renda * 2
    else:
        if (p_score >= 600) and (p_score <=799):
             p_limite = p_renda * 0.5
             if  p_limite >= 1000:
                 p_limite = p_renda * 0.5
             else:
                 p_limite = 1000
        else:
            if (p_score >= 300) and (p_score <= 599):
                 p_limite = 1000
            else:
                 p_limite = str('REPROVADO')



cursor.execute("""
INSERT INTO cadastro (nomeCompleto, idade, cpf, logradouro, numero, complemento, bairro, cidade, estado, renda, score, limite)
VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
""", (p_nomeCompleto, p_idade, p_cpf, p_logradouro, p_numero, p_complemento, p_bairro, p_cidade, p_estado, p_renda, p_score, p_limite))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
