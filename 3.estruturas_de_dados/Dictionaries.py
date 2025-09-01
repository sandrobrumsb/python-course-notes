# ---------------------------------------
# Estudo sobre Dictionaries (Dicionários) em Python
# ---------------------------------------

# 1. O que são Dicionários?
# - São usados para armazenar valores de dados em pares chave : valor.
# - É uma coleção ordenada*, mutável e não permite duplicatas.
# - Os dicionários são escritos com chaves {} e dentro têm "chaves" : "valores".
# - Os itens do dicionário são ordenados, alteráveis e não permitem duplicatas.
# - São mutáveis, o que significa que podemos alterar, adicionar ou remover itens depois que o dicionário for criado.


"""
# ---------------------------------------
# Métodos de Dicionário.
# O Python tem um conjunto de métodos integrados que você pode usar em dicionários:
# ---------------------------------------

Method         Description
clear()        Remove todos os elementos do dicionário
copy()         Retorna uma cópia do dicionário
fromkeys()     Retorna um dicionário com as chaves e valor especificados
get()          Retorna o valor da chave especificada
items()        Retorna uma lista contendo uma tupla para cada par chave-valor
keys()         Retorna uma lista contendo as chaves do dicionário
pop()          Remove o elemento com a chave especificada
popitem()      Remove o último par chave-valor inserido
setdefault()   Retorna o valor da chave especificada. Se a chave não existir: insere a chave com o valor especificado
update()       Atualiza o dicionário com os pares chave-valor especificados
values()       Retorna uma lista com todos os valores do dicionário

"""

esse_dicionario = {
    "brand": "Ford", 
    "model": "Mustang", 
    "year": 1964
}
print(esse_dicionario)

# Imprima o valor da "marca" do dicionário:
dicionario = {
    "marca": "Ford",
    "model": "Mustang", 
    "year": 1964
}
print(dicionario["marca"])

# Os dicionários não podem ter dois itens com a mesma chave:
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(dicionario) # Resultado: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Comprimento do dicionário:
print(len(dicionario))

# Itens do Dicionário - Tipos de Dados.
# Os valores nos itens do dicionário podem ser de qualquer tipo de dados:

dicionario = {
  "brand": "Ford", #string
  "electric": False, #boolean
  "year": 1964, #int
  "colors": ["red", "white", "blue"] #list
}
print(dicionario)

# Imprima o tipo de dados de um dicionário:
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(dicionario)) #Resultado: <class 'dict'>

# O construtor dict() - Usando o método dict() para criar um dicionário:
dicionario = dict(name = "John", age = 36, country = "Norway")
print(dicionario)


# 2. Python - Acessando Itens do Dicionário: 
# Acessando Itens - Obtenha o valor da chave "model":
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dicionario["model"]
print(x)

# O método get() lhe dará o mesmo resultado:
x = dicionario.get("model") 
print(x)

# Obtendo chaves - O método keys() retornará uma lista de todas as chaves no dicionário.
x = dicionario.keys()
print(x)

# Obter valores - O método values() retornará uma lista de todos os valores no dicionário:
x = dicionario.values()
print(x)

# Obter itens - O método items() retornará cada item em um dicionário (chave,valor), como tuplas em uma lista:
x = dicionario.items()

# Adicione um novo item ao dicionário original e veja se a lista de chaves também é atualizada:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #antes da mudança

car["color"] = "white"
print(x) #depois da mudança


# Faça uma alteração no dicionário original e veja se a lista de valores também é atualizada:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change

car["year"] = 2020
print(x) #after the change


# Faça uma alteração no dicionário original e veja se a lista de itens também é atualizada:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

# Adicione um novo item ao dicionário original e veja se a lista de itens também é atualizada:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change

car["color"] = "red"
print(x) #after the change

# Verifique se a chave existe - Para determinar se uma chave especificada está presente em um dicionário, use a inpalavra-chave:
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in dicionario:
  print("Sim, 'model' e uma das chaves no dicionário")

# 3. Python - Alterar itens do dicionário
# Alterar valores - Você pode alterar o valor de um item específico consultando seu nome de chave:

dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicionario["year"] = 2018
print(dicionario)

# O método update() - atualizará o dicionário com os itens do argumento fornecido:
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicionario.update({"year": 2020})
print(dicionario)

# 4. Python - Adicionar itens do dicionário:

# A adição de um item ao dicionário é feita usando uma nova chave de índice e atribuindo um valor a ela:
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicionario["color"] = "red"
print(dicionario)
 
# O método update() atualizará o dicionário com os itens de um argumento fornecido.
# Se o item não existir, ele será adicionado.
# O argumento deve ser um dicionário ou um objeto iterável com pares chave:valor:

dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicionario.update({"color": "red"})
print(dicionario)

# 5. Python - Remover Itens do Dicionário.
# O método pop() remove o item com o nome de chave especificado:
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicionario.pop("model")
print(dicionario)

# O método popitem() remove o último item inserido: 
# (em versões anteriores à 3.7, um item aleatório é removido):
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicionario.popitem()
print(dicionario)

# A palavra-chave "del" remove o item com o nome da chave especificado:
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del dicionario["model"]
print(dicionario)

# A palavra-chave  "del" também pode excluir completamente o dicionário:
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del dicionario
print(dicionario) # isso causará um erro porque "dicionario" não existe mais.

# O método clear() esvazia o dicionário:
dicionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicionario.clear()
print(dicionario)

# 6. - Python - Loop de Dicionários
# Você pode percorrer um dicionário usando um forloop: 
dicionario =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in dicionario:
  print(x) # OBS: Ao executar um loop em um dicionário, o valor de retorno são as chaves do dicionário.

# Imprima todos os valores no dicionário, um por um:
dicionario =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in dicionario:
  print(dicionario[x])

# Você também pode usar o values()método para retornar valores de um dicionário:
dicionario =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in dicionario.values():
  print(x)

# Você pode usar o método keys() para retornar as chaves de um dicionário:
dicionario =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in dicionario.keys():
  print(x)

# Faça um loop mostrando chaves e valores usando o método items():
dicionario =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in dicionario.items():
  print(x, y)

# 7. - Python - Copiar Dicionários:
"""
OBS:Você não pode copiar um dicionário simplesmente digitando dict2 = dict1, porque: dict2será apenas uma referência a dict1, e as alterações feitas em dict1serão feitas automaticamente também em dict2.
""" 
# Faça uma cópia de um dicionário com o método copy():
dicionario_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicionario_2 = dicionario_1.copy()
print(dicionario_2)

# Outra maneira de fazer uma cópia é usar a função interna dict():
dicionario_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dicionario_2 = dict(dicionario_1)
print(dicionario_2)

# 8. - Python - Dicionários Aninhado:
# Um dicionário pode conter nele dicionários, isso é chamado de dicionários aninhados.
familia = {
  "crianca_1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "crianca_2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "crianca_3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(familia)

# Adicionar três dicionários em um novo dicionário:
crianca_1 = {
  "name" : "Emil",
  "year" : 2004
}
crianca_2 = {
  "name" : "Tobias",
  "year" : 2007
}
crianca_3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : crianca_1,
  "child2" : crianca_2,
  "child3" : crianca_3
}
print(myfamily)

# Acessar itens em dicionários aninhados:
linguagens = {
  "linguagem_1" : {
    "name" : "Python",
    "year" : 2004
  },
  "linguagem_2" : {
    "name" : "Java",
    "year" : 2007
  },
  "linguagem_3" : {
    "name" : "C#",
    "year" : 2011
  }
}
print(linguagens["linguagem_2"]["name"])

# Percorrer dicionários aninhados - usando o método items():
linguagens = {
  "linguagem_1" : {
    "name" : "Python",
    "year" : 2004
  },
  "linguagem_2" : {
    "name" : "Java",
    "year" : 2007
  },
  "linguagem_3" : {
    "name" : "C#",
    "year" : 2011
  }
}
for x, obj in linguagens.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])