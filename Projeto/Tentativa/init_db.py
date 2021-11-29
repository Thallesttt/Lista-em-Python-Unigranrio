import sqlite3 as Banco
session = Banco.connect("Unigranrio.db")
#with Banco.Connect("database.db") as session:
with open("schema.sql")as file:
    session.executescript(file.read())
#with open("Schema Usuario.sql") as usuario:
#    session.executescript(usuario.read())
cursor = session.cursor() 
cursor.execute("INSERT INTO TB_USUARIO (ID,NOME,SENHA) VALUES(1,'Thalles','Thalles')")
session.commit()
session.close()