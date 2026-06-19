from flask import Flask, render_template
from utils import db
import os
from flask.Migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_username = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

conexao = f"mysql+pymysql://{db_username}:{db_senha}@{db_host}:{db_port}/{db_database}"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/faleconosco')
def faleconosco():
    return render_template('faleconosco.html')

@app.route('/avaliacoes')
def avaliacoes():
    return render_template('avaliacoes.html')

@app.route('/promocoes')
def promocoes():
    return render_template('promocoes.html')

@app.route('/login')
def login():
    return render_template('login.html')