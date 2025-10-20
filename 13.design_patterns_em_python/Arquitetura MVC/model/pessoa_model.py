"""
Model — a parte dos dados:

 - Onde ficam os dados e as regras de negócio.
 - Exemplo: A classe que acessa o banco de dados ou faz cálculos

"""


# Aqui temos um “modelo” de pessoa com uma regra de negócio (pode_votar):
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def pode_votar(self):
        return self.idade >= 16
