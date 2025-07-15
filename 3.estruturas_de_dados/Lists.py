# ---------------------------------------
# Estudo sobre Listas em Python
# ---------------------------------------

"""
Existem quatro tipos de dados de coleção na linguagem de programação Python:

List       -  É uma coleção que é ordenada e mutável. Permite membros duplicados.
Tuple      -  É uma coleção que é ordenada e imutável. Permite membros duplicados.
Set        -  É uma coleção que não é ordenada, imutável* e não indexada. Não permite membros duplicados.
Dicionário -  É é uma coleção que é ordenada** e mutável. Não permite membros duplicados.
"""

# 1. Tipos de coleções em Python:
# - List:   ordenada, mutável, permite duplicatas.
# - Tuple:  ordenada, imutável, permite duplicatas.
# - Set:    não ordenada, imutável*, não indexada, sem duplicatas.
# - Dict:   ordenado**, mutável, sem duplicatas.

# 2. Introdução às Listas
# Listas armazenam múltiplos itens em uma única variável.
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Listas podem conter itens duplicados.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Tamanho da lista com len()
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Listas podem conter diferentes tipos de dados
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# Verificando o tipo
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# Criando lista com list()
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# 3. Acessando Itens
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # Acesso por índice
print(thislist[-1])  # Indexação negativa

# Fatiamento
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

# Verificar se item existe
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# 4. Modificar Itens
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Alterar intervalo de valores
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Substituir por mais ou menos itens
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# 5. Inserir e Adicionar Itens
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange")
print(thislist)

# Estender com outra lista ou iterável
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# 6. Remover Itens
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

# del também pode excluir a lista inteira
thislist = ["apple", "banana", "cherry"]
del thislist

# clear() esvazia a lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# 7. Percorrer Listas

# Usando for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Usando range e len
for i in range(len(thislist)):
    print(thislist[i])

# Usando while
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# Compreensão de lista
[print(x) for x in thislist]

# 8. List Comprehension

# Sintaxe: [expressão for item in iterável if condição]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in fruits]
newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]
newlist = [x.upper() for x in fruits]
newlist = ["hello" for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]

# 9. Ordenar Listas

# Alfanumérica
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Ordem decrescente
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


# Classificação personalizada
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Ordenar sem diferenciar maiúsculas de minúsculas
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverter lista
thislist.reverse()
print(thislist)

# 10. Cópias de Lista

# Usando copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Usando list()
mylist = list(thislist)
print(mylist)

# Usando slice
mylist = thislist[:]
print(mylist)

# 11. Juntar Listas

# Com +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Com append() em loop
list1 = ["a", "b", "c"]
for x in list2:
    list1.append(x)
print(list1)

# Com extend()
list1 = ["a", "b", "c"]
list1.extend(list2)
print(list1)

# 12. Métodos de Lista
"""
append()    - Adiciona item ao final
clear()     - Remove todos os itens
copy()      - Retorna uma cópia da lista
count()     - Conta quantas vezes um valor aparece
extend()    - Adiciona elementos de outro iterável
index()     - Retorna índice de um valor
insert()    - Insere item em posição específica
pop()       - Remove item por índice
remove()    - Remove item por valor
reverse()   - Inverte a lista
sort()      - Ordena a lista
"""
