from flask import Flask, request,redirect,url_for
from flask.templating import render_template
import sqlite3
# from asyncio import tasks

app= Flask(__name__)

#Index
@app.route("/")  
def index():
    return render_template("posts.html")
    
#@app.route("/<db_results>")  
#def show_index_results(db_results):
#    
#    return render_template("index.html",db_results)

#Login
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def try_login():
    
    user = request.form["login"]
    senha = request.form["senha"]
    conn = get_db_connection()
    sql,sqlfrom,sqlwhere = "SELECT A.NOME, A.SENHA " +"\r\n", "FROM TB_USUARIO A " + "\r\n", f"WHERE A.NOME = '{user}' AND A.SENHA = '{senha}'"
    results = conn.execute(f"{sql}{sqlfrom}{sqlwhere}"+"\r\n"+" ORDER BY A.ID").fetchall()
    if len(results) > 0:
        return render_template(".login.html", db_results = results)
    return "error"

#Cadastro
@app.route("/cadastro")
def cadastro():
        return render_template("cadastro.html")

@app.route("/cadastro", methods=["POST"])
def cadastro_Post():
    if request.method == "POST":
        userName = request.form["Nome"]
        userSenha = request.form["Senha"]
        userBairro = request.form["Bairro"]
        userEndereco = request.form["Endereco"]
        userCep = request.form["Cep"]
        userEstado = request.form["Estado"]
        Values = f"'{userName}','{userSenha}','{userCep}','{userEndereco}','{userBairro}','{userEstado}'"
        connection = get_db_connection()
        insert = connection.execute(f"INSERT INTO TB_USUARIO (NOME,SENHA,CEP,ENDERECO,BAIRRO,ESTADO) VALUES({Values})")
        connection.commit()
        connection.close()

    return render_template('login.html')
     

@app.route("/bank")
def Bank():
    conn = get_db_connection()
    results = conn.execute('SELECT * FROM TB_USUARIO').fetchall()
    conn.close()
    return render_template('index.html', db_results = results)


def get_db_connection():
    conn = sqlite3.connect('Unigranrio.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/sad",methods=["GET","POST"])
def sad():
    return "OK"

@app.route("/mapa")
def mapa():
    return render_template("mapa.html")

@app.route("/posts")
def posts():
    return render_template("posts.html")

@app.route("/post/1")
def post1():
    return render_template("post1.html")

@app.route("/quizz/1")
def quizz1():
    return render_template("quizz1.html")

@app.route("/quizz/2")
def quizz2():
    return render_template("quizz2.html")

@app.route("/quizz/3")
def quizz3():
    return render_template("quizz3.html")

@app.route("/quizz/parabens")
def quizz_parabens():
    return render_template("quizz_parabens.html")

@app.route("/error")
def error():
    return "error"
