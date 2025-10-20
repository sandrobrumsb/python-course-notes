"""
Controller — liga a Model com a View:

 - Onde fica a lógica que liga o Model e a View.
 - O Controller usa o Model para executar a lógica e chama a View para mostrar o resultado.
 - EX: Recebe uma requisição, busca dados e devolve a resposta

"""

from model.pessoa_model import Pessoa
from view.pessoa_view import PessoaView


# O Controller cria o objeto (Model) e pede pra View exibir os dados.
class PessoaController:
    def criar_pessoa(self, nome, idade):
        pessoa = Pessoa(nome, idade)
        PessoaView.mostrar_detalhes(pessoa)
