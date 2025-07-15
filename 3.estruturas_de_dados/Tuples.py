# ---------------------------------------
# Estudo sobre Tuplas em Python
# ---------------------------------------

# 1. O que são tuplas?
# - Tipo de dado usado para armazenar múltiplos itens em uma única variável.
# - Coleção ordenada, imutável e que permite valores duplicados.
# - Faz parte dos 4 tipos de coleções embutidas no Python: List, Set, Dict e Tuple.

thistuple = ("apple", "banana", "cherry", "banana", "banana")
print(thistuple)

# 2. Verificando o comprimento da tupla
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  # Saída: 3

# 3. Criando uma tupla com um único item
# Observação: deve haver uma vírgula para ser considerada uma tupla
thistuple = ("apple",)
print(thistuple)

# 4. Tipos de dados em tuplas
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# 5. Tupla com tipos diferentes
tuple4 = ("abc", 34, True, 40, "male")

# 6. Verificando o tipo de dado
mytuple_type = ("apple",)
print(type(mytuple_type))  # <class 'tuple'>

# 7. Usando o construtor tuple()
tupla_vazia = tuple()
print(tupla_vazia)  # ()

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

lista_para_tupla = [1, 2, 3, 4]
tupla = tuple(lista_para_tupla)
print(tupla)

string_para_tupla = "abc"
tupla = tuple(string_para_tupla)
print(tupla)  # ('a', 'b', 'c')

# 8. Acessando itens de uma tupla
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # banana
print(thistuple[-1])  # cherry

# 9. Fatiamento de tuplas (slicing)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Índices 2 a 4
print(thistuple[:4])  # Início até índice 3
print(thistuple[2:])  # Do índice 2 até o fim
print(thistuple[-4:-1])  # De -4 a -2

# 10. Verificando se um item existe
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Sim, 'apple' está na tupla de frutas.")

# 11. Tuplas são imutáveis, mas há alternativas

# Alterar valor convertendo para lista
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Adicionar item - convertendo para lista
adicionar_tupla = ("apple", "banana", "cherry")
y = list(adicionar_tupla)
y.append("laranja")
adicionar_tupla = tuple(y)
print(adicionar_tupla)

# Adicionar item - concatenando com outra tupla
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# Remover item - convertendo para lista
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Excluir a tupla completamente
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # Isso causará erro: a tupla foi deletada

# 12. Descompactando uma Tupla
"""Quando criamos uma tupla, normalmente atribuímos valores a ela. Isso é chamado de "empacotamento" de uma tupla:
EX: fruits = ("apple", "banana", "cherry")
Mas, em Python, também podemos extrair os valores de volta para variáveis. Isso se chama "descompactação":
"""
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Desempacotamento com asterisco (*):
"""Quando você usa * em uma variável durante o desempacotamento, ela captura todos os valores restantes (como uma lista)."""

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(green)  # Resultado: apple
print(yellow)  # Resultado: banana
print(red)  # Resultado: ['cherry', 'strawberry', 'raspberry']

# Quando você coloca o * em uma outra variável, o Python vai colocar nela todos os valores que sobrarem, até que dê para preencher as outras variáveis que ainda faltam:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)  # Resultado: apple
print(tropic)  # Resultado: ['mango', 'papaya', 'pineapple']
print(red)  # Resultado: cherry

# 13. forloop em uma Tupla.
essa_tupla = ("apple", "banana", "cherry")
# Para cada fruta dentro da tupla...
for fruta in essa_tupla:
    # ...mostre essa fruta
    print(fruta)  # Resultado: apple banana cherry

# Mostra cada item da tupla, passando por todas as posições dela, uma por uma com base no indice (i):
essa_tupla = ("apple", "banana", "cherry")
for indice in range(len(essa_tupla)):
    print(essa_tupla[indice])

# Usando um loop While:
thistuple = ("apple", "banana", "cherry")
indice = 0
while indice < len(thistuple):
    print(thistuple[indice])
    indice = indice + 1


# 14. Join Tuplas:
# Para unir duas ou mais tuplas você pode usar o + operador:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Multiplicando tuplas:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


# 15. Métodos de tupla:
# count() - Retorna o número de vezes que um valor especificado ocorre em uma tupla
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)  # Resultado: 2

# index() - Pesquisa na tupla por um valor especificado e retorna a posição onde ele foi encontrado:
# OBS: O método index() encontra a primeira ocorrência do valor especificado
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)  # Resultado: 3
