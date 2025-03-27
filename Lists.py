
"""
Existem quatro tipos de dados de coleção na linguagem de programação Python:

List é uma coleção que é ordenada e mutável. Permite membros duplicados.
Tuple é uma coleção que é ordenada e imutável. Permite membros duplicados.
Set é uma coleção que não é ordenada, imutável* e não indexada. Nenhum membro duplicado.
Dicionário é uma coleção que é ordenada** e mutável. Sem membros duplicados.
"""

"""
Lista: são usadas para armazenar vários itens em uma única variável.
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)

#Como as listas são indexadas, elas podem ter itens com o mesmo valor:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Comprimento da lista, use a função len():
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Os itens da lista podem ser de qualquer tipo de dados:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Uma lista pode conter diferentes tipos de dados:
list1 = ["abc", 34, True, 40, "male"]

#Da perspectiva do Python, listas são definidas como objetos com o tipo de dados 'lista':
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Também é possível usar o construtor list() ao criar uma nova lista.
thislist = list(("apple", "banana", "cherry")) # observe os colchetes duplos
print(thislist)

#Imprima o segundo item da lista:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Indexação negativa significa começar do fim:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Faixa de índices - Você pode especificar um intervalo de índices especificando onde começar e onde terminar:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Deixar de fora o valor inicial, o intervalo começará no primeiro item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# Deixar de fora o valor inicial:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Especifique índices negativos se quiser iniciar a pesquisa a partir do final da lista:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Verifique se o item existe:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Para alterar o valor de um item específico, consulte o número do índice:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Alterar um intervalo de valores de itens:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Altere o segundo valor substituindo-o por dois novos valores:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Altere o segundo e o terceiro valor substituindo-os por um valor:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# O método insert()insere um item no índice especificado ex: posição 2, "watermelon":
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#Para adicionar um item ao final da lista, use o método append():
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Para acrescentar elementos de outra lista à lista atual, use o método extend():
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""
O método extend() não precisa anexar listas , 
você pode adicionar qualquer objeto iterável (tuplas, conjuntos, dicionários etc.).
"""
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#O método remove() remove o item especificado:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Se houver mais de um item com o valor especificado, o remove()método remove a primeira ocorrência:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# O método pop() remove o índice especificado:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Se você não especificar o índice, o pop()método removerá o último item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#A palavra-chave del também remove o índice especificado:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#A palavra-chave del também pode excluir a lista completamente.
thislist = ["apple", "banana", "cherry"]
del thislist

#O método clear() esvazia a lista:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Você pode percorrer os itens da lista usando um for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop pelos números de índices: 
# ranger() determina o quanto ele vai correr no for de acordo com o tamanho da lista len()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Você pode percorrer os itens da lista usando um whileloop,
#Use a len()função para determinar o comprimento da lista,
#comece em 0 e percorra os itens da lista consultando seus índices.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#A Compreensão de Lista oferece a sintaxe mais curta para percorrer listas:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#Com a compreensão de lista você pode fazer criar uma nova lista 
# sem o FOR tudo isso com apenas uma linha de código:
"""
A Sintaxe:
newlist = [expressão for item in iterável if condition == True]

"""
#Essa nova lista so tem a letra "a" no nome:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# apenas itens que não sejam "apple":
newlist = [x for x in fruits if x != "apple"]

#Sem declaração if:
newlist = [x for x in fruits]

# Você pode usar a range()função para criar um iterável:
#O iterável pode ser qualquer objeto iterável, como uma lista, tupla, conjunto etc.
newlist = [x for x in range(10)]

#Mesmo exemplo, mas com uma condição:
newlist = [x for x in range(10) if x < 5]

#Defina os valores na nova lista para letras maiúsculas:
newlist = [x.upper() for x in fruits]

#Defina todos os valores na nova lista como 'hello':
newlist = ['hello' for x in fruits]

#A expressão também pode conter condições, não como um filtro, mas como uma forma de manipular o resultado:
#"Devolva o item se não for banana, se for banana devolva laranja":
newlist = [x if x != "banana" else "orange" for x in fruits]

#Objetos de lista têm um método sort() que classificará a lista alfanumericamente:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Ordenar em ordem decrescente:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Classifique a lista com base na proximidade do número de 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#classificação da lista que não diferencia maiúsculas de minúsculas:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Inverta a ordem dos itens da lista:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Faça uma cópia de uma lista com o método copy():
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Outra maneira de fazer uma cópia é usar o método interno list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Você também pode fazer uma cópia de uma lista usando o :operador (slice).
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Junte-se a duas listas:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Acrescente list2 em list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Use o método extend() para adicionar list2 no final de list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

"""
Descrição dos métodos:
append() Adiciona um elemento no final da lista
clear() Remove todos os elementos da lista
copy() Retorna uma cópia da lista
count() Retorna o número de elementos com o valor especificado
extend() Adiciona os elementos de uma lista (ou qualquer iterável) ao final da lista atual
index() Retorna o índice do primeiro elemento com o valor especificado
insert() Adiciona um elemento na posição especificada
pop() Remove o elemento na posição especificada
remove() Remove o item com o valor especificado
reverse() Inverte a ordem da lista
sort() Classifica a lista
"""

