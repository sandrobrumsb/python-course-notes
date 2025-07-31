# ---------------------------------------
# Estudo sobre Sets (conjuntos) em Python
# ---------------------------------------

# 1. O que são Sets(conjuntos)?
# - Tipo de coleções de elementos únicos.
# - Não possuem uma ordem específica.
# - Conjuntos são usados para armazenar vários itens em uma única variável.
# - Conjuntos são semelhantes a listas, mas com a diferença crucial de que não permitem elementos duplicados.
# - Coleção não ordenada, imutável* e nao indexada.
# - Faz parte dos 4 tipos de coleções embutidas no Python: List, Set, Dict e Tuple.

conjunto = {"apple", "banana", "cherry"}
print(conjunto)

# -  Duplicatas não permitidas:
conjunto = {"apple", "banana", "cherry", "apple"}
print(conjunto)

# - True e 1 é considerado o mesmo valor:
# - Os valores True e 1são considerados o mesmo valor em conjuntos e são tratados como duplicados:
conjunto = {"apple", "banana", "cherry", True, 1, 2}
print(conjunto)
# - Nota: Os valores False e 0 são considerados o mesmo valor em conjuntos e são tratados como duplicados:
conjunto = {"apple", "banana", "cherry", False, True, 0}
print(conjunto)

# 2. Comprimento de um conjunto:
# - use a len() função.
conjunto = {"apple", "banana", "cherry"}
print(len(conjunto))

# 3. Itens do Conjunto - Tipos de Dados:
# - Tipos de dados string, int e booleanos:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# - Um conjunto pode conter diferentes tipos de dados:
# - strings, inteiros e valores booleanos:
set1 = {"abc", 34, True, 40, "male"}

# - Qual é o tipo de dado de um conjunto?
tipo_do_conjutno = {"apple", "banana", "cherry"}
print(type(tipo_do_conjutno))

# 4.  Usando o construtor set() para criar um conjunto:
conjunto = set(("apple", "banana", "cherry"))  # Observe os colchetes duplos*
print(conjunto)

# 5. Python - Acessar Itens de Sets(Conjuntos):
# OBS: Você não pode acessar itens em um conjunto referindo-se a um índice ou uma chave.
# OBS: Mas você pode percorrer os itens do conjunto usando um for loop, ou perguntar se um valor especificado está presente em um conjunto, usando a inpalavra-chave.
# OBS: Depois que um conjunto é criado, você não pode alterar seus itens, mas pode adicionar novos itens.

conjunto = {"apple", "banana", "cherry", "L"}
for x in conjunto:
    print(x)

# Verifique se "banana" está presente no conjunto:
conjunto = {"apple", "banana", "cherry"}
print("banana" in conjunto)  # Resultado: True

# Verifique se "banana" NÃO está presente no conjunto:
conjunto = {"apple", "banana", "cherry"}
print("banana" not in conjunto)  # Resultado: False


# 6. Python - Add Set Items:
# OBS: Depois que um conjunto é criado, você não pode alterar seus itens, mas pode adicionar novos itens.
# OBS: Para adicionar um item a um conjunto, use o add() método .

# Adicionar um item a um conjunto:
conjunto = {"apple", "banana", "cherry"}
conjunto.add("orange")
print(conjunto)

# Para adicionar itens de outro conjunto ao conjunto atual, use o update() método:
conjunto_atual = {"apple", "banana", "cherry"}
outro_conjunto = {"pineapple", "mango", "papaya"}
conjunto_atual.update(outro_conjunto)
print(conjunto_atual)

# Adicionando qualquer objeto iterável (tuplas, listas, dicionários etc.):
conjunto = {"apple", "banana", "cherry"}
lista = ["kiwi", "orange"]
conjunto.update(lista)
print(conjunto)

# Remover um item a um conjunto, use remove()o método ou discard():
conjunto_remove = {"apple", "banana", "cherry"}
conjunto_remove.remove("banana")
print(conjunto_remove)

conjunto_discard = {"apple", "banana", "cherry"}
conjunto_discard.discard("banana")
print(conjunto_discard)

# Remova um item aleatório usando o pop() método:
conjunto = {"apple", "banana", "cherry"}
remover_item_aleatorio = conjunto.pop()
print(remover_item_aleatorio)
print(conjunto)

# O clear() método esvazia o conjunto:
conjunto = {"apple", "banana", "cherry"}
conjunto.clear()
print(conjunto)

# A palavra-chave del excluirá o conjunto completamente:
conjunto = {"apple", "banana", "cherry"}
del conjunto
print(conjunto)

# 7. Percorrer os itens de um Conjuntos usando um for loop:
conjunto = {"apple", "banana", "cherry"}
for x in conjunto:
    print(x)
# 8. Conjuntos de junção (Join Sets):
# OBS: Existem várias maneiras de unir dois ou mais conjuntos em Python.
# OBS: union()e update()unem todos os itens de ambos os conjuntos.
# OBS: Ambos, union() e update() excluirão quaisquer itens duplicados
# OBS: intersection() mantém SOMENTE as duplicatas.
# OBS: difference() mantém os itens do primeiro conjunto que não estão nos outros conjuntos.
# OBS: symmetric_difference() mantém todos os itens EXCETO as duplicatas.


# union() retorna um novo conjunto com todos os itens de ambos os conjuntos:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Você pode usar o " | " operador em vez do union()método e obterá o mesmo resultado.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Juntando varios consjuntos com o union():
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Ao usar o "|" operador, separe os conjuntos com mais "|" operadores:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

# Juntando um conjunto com uma tupla:
# OBS: O "|" operador só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados.
conjunto = {"a", "b", "c"}
tupla = (1, 2, 3)
juntando_sets_com_tuples = conjunto.union(tupla)
print(juntando_sets_com_tuples)

# Atualizando consuntos - o método update() insere os itens do conjunto_1 no conjunto_2:
# OBS: update() método insere todos os itens de um conjunto em outro.
# OBS: Ele altera o conjunto original e não retorna um novo conjunto.
conjunto_1 = {"a", "b", "c"}
conjunto_2 = {1, 2, 3}

conjunto_1.update(conjunto_2)
print(conjunto_1)

# Interseção- O intersection()método retornará um novo conjunto, que contém apenas os itens que estão presentes em ambos os conjuntos:

conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {"google", "microsoft", "apple"}

conjunto_3 = conjunto_1.intersection(conjunto_2)
print(conjunto_3)  # Resultado: {'apple'}

# OBS: Você pode usar o &operador em vez do intersection()método e obterá o mesmo resultado:
# - O & operador só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o método intersection().
conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {"google", "microsoft", "apple"}

conjunto_3 = conjunto_1 & conjunto_2
print(conjunto_3)  # Resultado: {'apple'}

# intersection_update() também manterá SOMENTE as duplicatas, mas alterará o conjunto original em vez de retornar um novo conjunto:
conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {"google", "microsoft", "apple"}

conjunto_1.intersection_update(conjunto_2)

print(conjunto_1)  # Resultado: {'apple'}

# Os valores "True" e "1" são considerados o mesmo valor. O mesmo vale para "False" e "0":
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)  # Resultado: {False, 1, 'apple'}

# Diferença - difference() retornará um novo conjunto que conterá apenas os itens do primeiro conjunto que não estão presentes no outro conjunto:
conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {"google", "microsoft", "apple"}

conjunto_3 = conjunto_1.difference(conjunto_2)
print(conjunto_3)  # Resultado: {'banana', 'cherry'}

# OBS - Você pode usar o -operador em vez do difference()método e obterá o mesmo resultado:
# - O - operador só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o método difference().
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)  # Resultado: {'cherry', 'banana'}

# difference_update() Olha todos os elementos que estão tanto em conjunto_1 quanto em conjunto_2 e remove do conjunto_1 os itens que estao em consjunto_2.
conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {"google", "microsoft", "apple"}

conjunto_1.difference_update(conjunto_2)
print(conjunto_1)  # Resultado: {'banana', 'cherry'}


# Diferenças Simétricas - O symmetric_difference() manterá apenas os elementos que NÃO estão presentes em ambos os conjuntos.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)  # Resultado:{'microsoft', 'google', 'cherry', 'banana'}

# OBS: Você pode usar o ^operador em vez do symmetric_difference()método e obterá o mesmo resultado.
# -  O ^ operador só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o método symmetric_difference().
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# O symmetric_difference_update() também manterá tudo, exceto os itens duplicados, mas alterará o conjunto original em vez de retornar um novo conjunto:

conjunto_1 = {"apple", "banana", "cherry"}
conjunto_2 = {"google", "microsoft", "apple"}

conjunto_1.symmetric_difference_update(conjunto_2)
print(conjunto_1)  # Resultado: {'microsoft', 'banana', 'cherry', 'google'}


"""
---------------------------------------
# 9 . Lista de Métodos de Conjunto:
---------------------------------------

| Método                          | Atalho            | Descrição                                                                                 |
| ------------------------------- | ----------------- | ----------------------------------------------------------------------------------------- |
| `add()`                         | não possui atalho | Adiciona um elemento ao conjunto                                                          |
| `clear()`                       | não possui atalho | Remove todos os elementos do conjunto                                                     |
| `copy()`                        | não possui atalho | Retorna uma cópia do conjunto                                                             |
| `difference()`                  |       `-`         | Retorna um conjunto com a diferença entre dois ou mais conjuntos                          |
| `difference_update()`           |       `-=`        | Remove os itens deste conjunto que também estão em outro conjunto especificado            |
| `discard()`                     | não possui atalho | Remove o item especificado (sem erro se não existir)                                      |
| `intersection()`                |       `&`         | Retorna um conjunto que é a interseção entre dois conjuntos                               |
| `intersection_update()`         |        `&=`       | Remove os itens deste conjunto que não estão presentes nos outros conjuntos especificados |
| `isdisjoint()`                  | não possui atalho | Retorna se dois conjuntos não têm elementos em comum                                      |
| `issubset()`                    |       `<=`        | Retorna `True` se todos os itens deste conjunto estiverem em outro                        |
| —                               |       `<`         | Retorna `True` se todos os itens deste conjunto estiverem em outro maior                  |
| `issuperset()`                  |       `>=`        | Retorna `True` se todos os itens de outro conjunto estiverem neste                        |
| —                               |       `>`         | Retorna `True` se todos os itens de outro conjunto menor estiverem neste                  |
| `pop()`                         | não possui atalho | Remove um elemento do conjunto (de forma arbitrária)                                      |
| `remove()`                      | não possui atalho | Remove o elemento especificado (gera erro se não existir)                                 |
| `symmetric_difference()`        |       `^`         | Retorna um conjunto com os elementos diferentes entre dois conjuntos                      |
| `symmetric_difference_update()` |       `^=`        | Atualiza o conjunto com os elementos diferentes entre este e outro                        |
| `union()`                       |       `\|`        | Retorna um conjunto com a união de dois ou mais conjuntos                                 |
| `update()`                      |       `\|=`       | Atualiza o conjunto com a união entre este e outros conjuntos                             |

"""
