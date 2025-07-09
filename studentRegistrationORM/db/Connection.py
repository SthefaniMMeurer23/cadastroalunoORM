from peewee import SqliteDatabase
from pathlib import Path #biblioteca para lidar com diretorios, para evitar caminhos hard-code
import os

#define a raiz do projeto 
PROJECT_ROOT = Path(__file__).parent.parent 

#define onde sera criado o banco de dados
DB_DIR = PROJECT_ROOT/ "Databases"

#cria o diretorio se ele nao existir 
DB_DIR.mkdir(exist_ok=True)

#caminho completo para o arquivo.db (meu banco de dados)

DB_PATH = DB_DIR/ "students02.db"

#cria de fato o banco de dados
db =  SqliteDatabase(DB_PATH)

def connect_db():
    from models.student import Student #importar a classe student da pasta models
    db.connect() #abre conexao com o banco de dados
    db.create_tables([Student], safe=True)

def close_db(exception=None):
    if not db.is_closed():
        db.close()

    


