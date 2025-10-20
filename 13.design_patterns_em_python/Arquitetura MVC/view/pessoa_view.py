"""
View — a parte visual (saída para o usuário):
 - Onde fica a apresentação (o que o usuário vê).
 - Exemplo: Um arquivo HTML, um template ou saída no terminal

"""


# A view só mostra informações — nunca faz cálculos ou regras.
class PessoaView:
    @staticmethod
    def mostrar_detalhes(pessoa):
        print(f"Nome: {pessoa.nome}")
        print(f"Idade: {pessoa.idade}")
        if pessoa.pode_votar():
            print("Pode votar ✅")
        else:
            print("Não pode votar ❌")
