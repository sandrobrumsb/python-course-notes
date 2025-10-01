"""
JSON é uma sintaxe para armazenar e trocar dados.
JSON é texto escrito com notação de objeto JavaScript.

"""

# 1. JSON em Python
# O Python tem um pacote integrado chamado json, que pode ser usado para trabalhar com dados JSON.

# Exemplo - Importe o módulo json:

import json

# Converter de JSON para Python:
# Se você tiver uma string JSON, poderá analisá-la usando o json.loads().


import json

# some JSON:
x = '{ "name":"John", ' '"age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# O resultado será um dicionário Python:
print(y["age"])


# Converter de Python para JSON
# Se você tiver um objeto Python,
# poderá convertê-lo em uma string JSON usando o json.dumps()
# Exemplo - Converter de Python para JSON:

import json

# a Python object (dict):
x = {"name": "John", "age": 30, "city": "New York"}

# convert into JSON:
y = json.dumps(x)

# o resultado será um JSON:
print(y)

"""
Você pode converter objetos Python dos seguintes tipos em strings JSON:
dict
list
tuple
string
int
float
True
False
None

"""
# Exemplo - Converta objetos Python em strings JSON e imprima os valores:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


"""
OBS: Quando você converte de Python para JSON, os objetos Python são convertidos no equivalente JSON (JavaScript):

Python	    JSON
dict	    Object
list	    Array
tuple	    Array
str	        String
int	        Number
float	    Number
True	    true
False	    false
None	    null
"""

# Exemplo - Converta um objeto Python contendo todos os tipos de dados legais:

import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

print(json.dumps(x))


# Formatar o resultado
# O exemplo acima imprime uma string JSON, mas não é muito fácil de ler, sem recuos e quebras de linha.
# O json.dumps() possui parâmetros para facilitar a leitura do resultado:

# Exemplo - Use o indentparâmetro para definir o número de recuos:
import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))


# Ordenar o Resultado
# O json.dumps() possui parâmetros para ordenar as chaves no resultado:
# Exemplo - Use o sort_keys para especificar se o resultado deve ser classificado ou não:
import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

# classificar o resultado em ordem alfabética por chaves:
print(json.dumps(x, indent=4, sort_keys=True))
