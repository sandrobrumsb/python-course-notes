# Importa o módulo os para operações relacionadas ao sistema operacional
import os


class Config:
    """
    Classe de configuração para a aplicação Flask.
    Define as variáveis de configuração do banco de dados, rastreamento e chave secreta.
    """

    # String de conexão com o banco de dados SQLite
    SQLALCHEMY_DATABASE_URI = "sqlite:///user.db"

    # Desativa o rastreamento de modificações do SQLAlchemy para economizar recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Chave secreta para segurança da aplicação (ex: sessões, cookies)
    SECRET_KEY = os.urandom(24)
