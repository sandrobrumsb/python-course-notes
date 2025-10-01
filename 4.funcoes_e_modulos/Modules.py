"""
O que é um módulo?
    - Considere um módulo como sendo o mesmo que uma biblioteca de código.
    - Um arquivo contendo um conjunto de funções que você deseja incluir em seu aplicativo.

"""

# 1. Criar um módulo -
# Exemplo - Importe o módulo chamado meu_modulo e chame a função de apresentacao:


import meu_modulo

meu_modulo.apresentacao("Sandro")

# 2. Variáveis ​​no Módulo
# O módulo pode conter funções, mas também variáveis ​​de todos os tipos (matrizes, dicionários, objetos etc.)
# Exemplo - Salve este código no meu_modulo.py | Importe o módulo chamado mymodule e acesse o dicionário person1:


import meu_modulo

a = meu_modulo.pessoa["idade"]
print(a)


# 3 . Nomeando um Módulo | Renomeando um módulo
# Você pode nomear o arquivo do módulo como quiser, mas ele deve ter a extensão de arquivo .py
# Você pode criar um alias ao importar um módulo, usando a palavra-chave "as":
# Exemplo - Crie um alias para meu_modulo mx:

import meu_modulo as mx

a = mx.pessoa["idade"]
print(a)


# 4. Módulos integrados
# Existem vários módulos integrados no Python, que você pode importar quando quiser.
# Exemplo - Importe e use o módulo platform:
import platform

x = platform.system()
print(x)


# 5. Usando a função dir()
# Existe uma função interna para listar todos os nomes de funções (ou nomes de variáveis) em um módulo.
# A função dir():
#  Exemplo - Listar todos os nomes definidos pertencentes ao módulo da plataforma:
import platform

x = dir(platform)
print(x)


# Importar do módulo
# Você pode escolher importar apenas partes de um módulo usando a palavra-chave from.
# Exemplo - O módulo nomeado mymodule tem uma função e um dicionário..
# Importe apenas o dicionário person1 do módulo:
from meu_modulo import pessoa

print (pessoa["idade"])

