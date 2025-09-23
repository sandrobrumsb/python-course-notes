"""
Arrays [Matrizes] Python:

 - Observação: o Python não tem suporte integrado para matrizes, mas listas do Python podem ser usadas.
 - Observação: esta página mostra como usar LISTAS como ARRAYS;
 - Para trabalhar com arrays em Python, você terá que importar uma biblioteca, como a biblioteca NumPy .

 - O que é um Array?
 - Um array é uma variável especial que pode conter mais de um valor por vez.
 - Matrizes são usadas para armazenar vários valores em uma única variável:

"""

"""
Métodos usados em matriz:

# append() - Adiciona um elemento no final da lista
# clear() - Remove todos os elementos da lista
# copy() - Retorna uma cópia da lista
# count() - Retorna o número de elementos com o valor especificado
# extend() - Adiciona os elementos de uma lista (ou qualquer iterável) no final da lista atual
# index() - Retorna o índice do primeiro elemento com o valor especificado
# insert() - Adiciona um elemento na posição especificada
# pop() - Remove o elemento na posição especificada
# remove() - Remove o  item  pelo nome do valor
# reverse() - Inverte a ordem da lista
# sort() - Ordena a lista

"""

# 1. Matrizes são usadas para armazenar vários valores em uma única variável:
# Exemplo - Crie uma matriz contendo nomes de carros:

from numpy import append


cars = ["Ford", "Volvo", "BMW"]

# 2. Acesse os elementos de uma matriz.
# Exemplo - Obtenha o valor do primeiro item da matriz:

matriz_carro = ["Ford", "Volvo", "BMW"]
x = matriz_carro[1]
print(x)

# Modifique o valor do primeiro item da matriz:
matriz_carro = ["Ford", "Volvo", "BMW"]
matriz_carro[0] = "Bicicleta"
print(matriz_carro)

# 3. O comprimento de uma matriz.
matriz_carro = ["Ford", "Volvo", "BMW"]
x = len(matriz_carro)
print(x)

# 4. Elementos de matriz de loop.
# Você pode usar o for in para percorrer todos os elementos de uma matriz.
matriz_carro = ["Ford", "Volvo", "BMW"]
for x in matriz_carro:
    print(x)

# 5. Adicionando elementos de matriz
# Você pode usar o método append() para adicionar um elemento a uma matriz.
# Exemplo - Adicione mais um elemento à matriz matriz_carro:
matriz_carro = ["Ford", "Volvo", "BMW"]
matriz_carro.append("Ferrari")
print(matriz_carro)

# 6. Removendo elementos do array
# Você pode usar o método pop() para remover um elemento do array de acordo com a posição:
# Exemplo - Exclua o segundo elemento da matriz matriz_carro:
matriz_carro = ["Ford", "Volvo", "BMW"]
matriz_carro.pop(1)
print(matriz_carro)

# Você também pode usar o método remove() para remover um elemento do array pelo nome do valor:
matriz_carro = ["Ford", "Volvo", "BMW"]
matriz_carro.remove("BMW")
print(matriz_carro)
