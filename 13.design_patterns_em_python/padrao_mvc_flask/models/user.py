# Importa a extensão SQLAlchemy para integração com o banco de dados
# Necessario isntalar atraves do: pip install Flask Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Instancia o objeto db para manipulação do banco de dados
db = SQLAlchemy()


# Classe User criar a tabela de usuários no banco de dados
class User(db.Model):
    __tablename__ = "users"  # Define o nome da tabela no banco de dados / se nao for feito isso o nome ta tabela seria o nome da Classe.

    # Chave primária, identificador único do usuário
    id = db.Column(db.Integer, primary_key=True)
    # Nome do usuário, campo obrigatório
    name = db.Column(db.String(100), nullable=False)
    # E-mail do usuário, campo obrigatório e único
    email = db.Column(db.String(100), unique=True, nullable=False)
