import os
from flask import Flask  # Importa a classe Flask do pacote flask
from config import Config  # Importa a classe de configuração definida em config.py
from controllers.user_controller import UserController
from models.user import db

# Criando uma instância da aplicação Flask
app = Flask(__name__, template_folder=os.path.join("view", "template"))
app.config.from_object(Config)  # Carrega as configurações da classe Config

# criando uma rota da classe que esta em ./controllers:
app.add_url_rule("/", "index", UserController.index)

# criando uma nova rota na aplicação:
# ("/nome_da_rota", "nome_da_funcao_chamada", localização_da_função.nome_da_funcao, metodos_a_usar)
app.add_url_rule("/contact", "contact", UserController.contact, methods=["GET", "POST"])

# Integrando/Inicializando o Bando de Dados em ./models:
db.init_app(app)
# criando as tabelas do db:
with app.app_context():
    db.create_all()

# Ponto de entrada da aplicação -> Inicia o servidor Flask em modo debug:
if __name__ == "__main__":
    app.run(debug=True)
