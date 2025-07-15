from pickle import GET
from flask import Flask, make_response, jsonify, request
from bd import Carros #importanto o banco de dados(bd.py)


# __name__: assume o nome do modulo principal caso nao queira dar um nome a api do flask.
app = Flask(__name__)

# Desabilita a ordenação padrao do json, no metodo post(opcional):
app.config['JSON_SORT_KEYS'] = False


#Criando uma rota para mostrar da api:
@app.route('/carros',methods=['GET'])
# Criando funçoes:
def get_carros ():
    return make_response(
        jsonify(
            mensagem= 'Lista de Carros.',
            dados= Carros
        )
        )

@app.route('/carros', methods=['POST'])
# Nova rota para salvar carros no BD:
def create_carro():
    carro = request.json
    Carros.append(carro) # append: pega e adiciona na ultima posição
    return make_response(
        jsonify(
            mensagem='Carro cadastrado com sucesso!',
            Carro= carro
        )
        )


# Starta a api, deixar ela disponivel:
app.run()