import sqlite3 as lite

con = lite.connect('dados.db')

# CRUD (create, escrever, update e delete)


# inserir dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

# atualizar dados
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query,i)

# Deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query,i)

# Ver dados
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

# Ver dados individual
def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)