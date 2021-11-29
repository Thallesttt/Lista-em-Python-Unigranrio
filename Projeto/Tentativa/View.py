from flask import Flask
from flask.templating import render_template
import sqlite3
# from asyncio import tasks

app= Flask(__name__)

@app.route("/")  
def index():
    return render_template("index.html")



@app.route("/Cadastro")
def cadastro():
     return render_template("cadastro.html")
    

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