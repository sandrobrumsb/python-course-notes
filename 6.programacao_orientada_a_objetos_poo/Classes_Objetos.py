"""
Classes/Objetos Python:

- Python é uma linguagem de programação orientada a objetos.
- Quase tudo em Python é um objeto, com suas propriedades e métodos.
- Uma classe é como um construtor de objetos ou um "projeto" para criar objetos.

"""

# 1. Criando uma Classe
# Para definir uma nova classe em Python, utilize a palavra-chave 'class'.
# Uma classe serve como um molde para criar objetos com propriedades e métodos.

class MinhaClasse:
    x = 5


print(MinhaClasse)


# Criando um objeto - Agora podemos utilizar a classe 'MinhaClasse' para instanciar objetos:
class MyClass:
    x = 5


# Instanciando um objeto chamado p1 a partir da classe MyClass
p1 = MyClass()

print(p1.x)



# 2. O método __init__():
# O método especial __init__() é chamado automaticamente sempre que um novo objeto da classe é criado.
# Ele serve para inicializar os atributos do objeto e executar qualquer configuração necessária.
# É equivalente ao "construtor" em outras linguagens orientadas a objetos.



# Definição de uma classe chamada "Pessoa"
class Pessoa:
    # O método __init__ inicializa os atributos 'nome' e 'idade' ao criar um novo objeto
    def __init__(self, nome, idade):
        # Atributo 'nome' = o valor passado
        self.nome = nome
        # Atributo 'idade'= com o valor passado
        self.idade = idade


# Criando um objeto da classe Pessoa, chamado p1, com nome "Sandro" e idade 36
p1 = Pessoa("Sandro", 36)

# Exibindo os atributos do objeto p1
print(p1.nome)  # Saída: Sandro
print(p1.idade)  # Saída: 36



# 3. O método __str__()
# O método especial __str__() define a representação em string de um objeto.
# Quando utilizamos print(objeto), o Python chama automaticamente o método __str__() da classe.



class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}({self.idade})"


p1 = Pessoa("Sandro", 36)
print(p1)



# 4. Criando Métodos
# Podemos definir métodos (funções) dentro de uma classe para realizar ações específicas com os dados do objeto.
# Métodos são funções que pertencem à classe e podem acessar/alterar os atributos do objeto.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método personalizado da classe Pessoa
    def minhaFuncao(self):
        print("Olá, meu nome é " + self.nome)


p1 = Pessoa("Sandro", 36)
p1.minhaFuncao()


# OBSERVAÇÃO:
# O parâmetro 'self' em métodos de instância é uma referência ao próprio objeto.
# Ele permite acessar atributos e outros métodos da mesma instância.



# 5. O parâmetro self
# O parâmetro 'self' é uma convenção em Python para se referir à instância atual da classe.
# Ele não precisa obrigatoriamente se chamar 'self', mas deve ser o primeiro parâmetro de qualquer método de instância.
# Exemplo: Usando nomes alternativos como "meuobjeto" e "abc" no lugar de 'self'.

class Pessoa:

    def __init__(meuobjeto, nome, idade):
        meuobjeto.nome = nome  # 'meuobjeto' faz o papel de 'self'
        meuobjeto.idade = idade

    def minhaFuncao(abc):  # 'abc' faz o papel de 'self'
        print("Olá, meu nome é: " + abc.nome)


p1 = Pessoa("Sandro", 36)
p1.minhaFuncao()



# 6. Modificando propriedades do objeto
# Podemos alterar os valores dos atributos de um objeto após sua criação.
# Exemplo: Definindo a idade de p1 como 37.

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def minhaFuncao(self):
        print("Olá, meu nome é " + self.nome)


p1 = Pessoa("John", 36)

p1.idade = 37
print(p1.idade)



# 7. Excluindo propriedades do objeto
# Podemos remover atributos de um objeto usando a palavra-chave 'del'.
# Exemplo: Excluindo a propriedade 'idade' do objeto p1.



class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def minhaFuncao(self):
        print("Olá, meu nome é " + self.nome)


p1 = Pessoa("John", 36)


del p1.idade  # Excluindo o atributo 'idade' do objeto p1

print(p1.idade)



# 8. Excluindo objetos
# Podemos remover completamente um objeto da memória usando a palavra-chave 'del'.
# Exemplo: Excluindo o objeto p1.

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def minhaFuncao(self):
        print("Olá, meu nome é " + self.nome)


p1 = Pessoa("John", 36)


del p1  # Excluindo o objeto p1 da memória

print(p1.idade)



# 9. A declaração 'pass'
# Definições de classe não podem estar vazias. Se precisar de uma classe vazia, utilize a instrução 'pass' para evitar erros de sintaxe.
# Exemplo:
class Pessoa:
    pass
