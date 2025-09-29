"""
Escopo Python:

- Uma variável só está disponível dentro da região em que foi criada. Isso é chamado de escopo .
"""


# 1. Função dentro da função
# Exemplo - A variável local pode ser acessada de uma função dentro da função:
def funcao():
    x = 300

    def funcao_interna():
        print(x)

    funcao_interna()


funcao()

# 2. Escopo global
# Uma variável criada no corpo principal do código Python é uma variável global e pertence ao escopo global.
# Variáveis ​​globais estão disponíveis em qualquer escopo
# Exemplo - Uma variável criada fora de uma função é global e pode ser usada por qualquer pessoa:

variavel_global = 300

def funcao():
  print(variavel_global)

funcao()

print(variavel_global)

# 3. Nomeando Variáveis
# Se você operar com o mesmo nome de variável dentro e fora de uma função,
# o Python as tratará como duas variáveis ​​separadas, 
# uma disponível no escopo global (fora da função) e outra disponível no escopo local (dentro da função):

# Exemplo - A função imprimirá o local (variavel_local), em seguida, o código imprimirá o global (variavel_global):
variavel_global = 100

def myfunc():
  variavel_local = 200
  print(variavel_local)

myfunc()

print(variavel_global)

# 4. Palavra-chave global
# Exemplo - Se você usar a palavra-chave "global", a variável pertence ao escopo global:
def funcao():
  global x
  x = 300

funcao()

print(x)    


# Exemplo - Para alterar o valor de uma variável global dentro de uma função, consulte a variável usando a palavra-chave global:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)


# 5. Palavra-chave não local
# A palavra-chave "nonlocal" é usada para trabalhar com variáveis ​​dentro de funções aninhadas.
# A nonlocal faz com que a variável pertença à função externa.

# Exemplo - Se você usar a nonlocal, a variável pertencerá à função externa:
def funcao1():
  x = "Jane"
  def funcao2():
    nonlocal x
    x = "hello"
  funcao2()
  return x

print(funcao1())
