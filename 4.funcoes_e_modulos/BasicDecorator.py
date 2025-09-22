"""
Decorador Básico:

- Permitem que você adicione comportamento extra a uma função, sem alterar o código da função..
- Um decorador é uma função que recebe outra função como entrada e retorna uma nova função.

"""

# 1. Exemplo: Um decorador básico que coloca em maiúsculas,
#  o valor de retorno da função decorada.


def mudar_maiusculo(func):
    def func_interna():
        return func().upper()  # Aplica a transformação de maiúsculas

    return func_interna  # Retorna a nova função modificada


@mudar_maiusculo  # Aqui estamos decorando a função
def minha_funcao():
    return "Olá Sally"  # Esta função retorna a string "Hello Sally"


print(minha_funcao())

# 2. Um decorador pode ser chamado várias vezes.
# Basta posicioná-lo acima da função que você deseja decorar:


def mudar_maiusculo(func):
    def func_interna():
        return func().upper()

    return func_interna


@mudar_maiusculo
def minha_funcao():
    return "Hello Sally"


@mudar_maiusculo
def outrafuncao():
    return "Tudo bem?"


print(minha_funcao())
print(outrafuncao())


# 3. Argumentos na Função Decorada:
# Funções com argumentos também podem ser decoradas:
def mudar_maiusculas(func):
  def func_interna(x):
    return func(x).upper()
  return func_interna

@mudar_maiusculas
def minha_funcao(nome): # passando o argumento nome
  return "Olá " + nome

print(minha_funcao("João")) #declanrando o argumento = Joao.


#4. Uma fábrica de decoradores é uma função que cria um decorador diferente,
#  dependendo do valor que você passar para ela:

def mudar_maiusculas_minusculas(n):
  def mudar_maiusculas_minusculas_func(func):
    def minha_interna():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return minha_interna
  return mudar_maiusculas_minusculas_func

@mudar_maiusculas_minusculas(1)
def minha_funcao():
  return "Olá Linus"

print(minha_funcao())

# 5. Vários Decoradores - Você pode usar vários decoradores em uma função.
# Isso é feito colocando as chamadas do decorador umas sobre as outras.

# Exemplo - Um decorador para letras maiúsculas e um para adicionar uma saudação:
def mudar_maiusculas(func):
  def minha_interna():
    return func().upper()
  return minha_interna

def adicionar_saudacao(func):
  def minha_interna():
    return "Olá " + func() + " Tenha um bom dia!"
  return minha_interna

@mudar_maiusculas
@adicionar_saudacao
def minha_funcao():
  return "Tobias"

print(minha_funcao())

# 6. Preservando Metadados de Função:
# Funções em Python têm metadados que podem ser acessados ​​usando os atributos __name__e .__doc__
# Exemplo - Normalmente, o nome de uma função pode ser retornado com o atributo __name__:

def minha_funcao():
  return "Tenha um bom dia!"

print(minha_funcao.__name__) # retornando o nome da funcao.


# Mas, quando uma função é decorada, os metadados da função original são perdidos.
# Exemplo 2 - Tente retornar o nome de uma função decorada e você não obterá o mesmo resultado:

def mudar_maiusculas(func):
  def minhafunc_interna():
    return func().upper()
  return minhafunc_interna

@mudar_maiusculas
def minha_funcao():
  return "Tenha um ótimo dia!"

print(minha_funcao.__name__)

# Para corrigir isso, o Python tem uma função interna chamada functools.wrapsque 
# pode ser usada para preservar o nome:

import functools

def mudar_maiusculas(func):
  @functools.wraps(func)
  def minhafunc_interna():
    return func().upper()
  return minhafunc_interna

@mudar_maiusculas
def minha_funcao():
  return "Tenha um ótimo dia!"

print(minha_funcao.__name__)



