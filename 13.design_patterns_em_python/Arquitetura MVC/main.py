"""
Arquivo principal — executa o app:

- O arquivo principal (main.py) só inicia o Controller — ele é o ponto de entrada, mas não participa da lógica.

O fluxo do MVC é assim:
Usuário → Controller → Model → Controller → View → Usuário

O usuário faz algo (por exemplo, executa main.py ou acessa uma rota no Flask).
O Controller recebe essa ação e decide o que fazer.
O Model executa a regra de negócio (buscar dados, calcular, salvar, etc).
O Controller pega o resultado do Model.
O View mostra o resultado ao usuário (terminal, HTML, etc).
"""

from controller.pessoa_controller import PessoaController

if __name__ == "__main__":
    controller = PessoaController()
    controller.criar_pessoa("Sandro", 25)
