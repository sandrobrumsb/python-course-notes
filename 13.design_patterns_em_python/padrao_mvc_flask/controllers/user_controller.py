# Importa a função render_template do Flask para renderizar arquivos HTML
import email
from flask import render_template, request, redirect, url_for
from models.user import User, db


# Controller responsável por lidar com as requisições relacionadas ao usuário
class UserController:
    @staticmethod  # define se o método será estático = pode chamar na classe sem criar uma instância.
    def index():
        """
        Método estático que retorna a página inicial (index.html).
        Utiliza o render_template para renderizar o template HTML.
        """
        # Busca todos os registros de usuários no banco de dados
        users = User.query.all()
        # Renderiza a página index.html, e passa a lista de usuários para o template
        return render_template("index.html", users=users)

    @staticmethod
    def contact():
        """
        Método responsável por exibir e processar o formulário de contato.
        - Se a requisição for POST, realiza o cadastro de um novo usuário no banco de dados.
        - Se a requisição for GET, apenas renderiza a página contact.html.

        """
        if request.method == "POST":
            # Recupera o valor do campo 'name' enviado pelo formulário
            name = request.form["name"]
            # Recupera o valor do campo 'email' enviado pelo formulário
            email = request.form["email"]

            # Cria uma nova instância de usuário com os dados do formulário
            new_user = User(name=name, email=email)
            # Adiciona o novo usuário à sessão do banco de dados
            db.session.add(new_user)
            # Salva (commita) as alterações no banco de dados
            db.session.commit()

            # Redireciona o usuário para a página inicial após o cadastro
            return redirect(url_for("index"))

        # Se a requisição for GET, apenas exibe o formulário de contato
        return render_template("contact.html")
