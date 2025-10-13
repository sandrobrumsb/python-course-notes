"""
Python RegEx:
 - Uma RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
 - RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado.

    Funções RegEx:

findall: Retorna uma lista contendo todas as correspondências.
search: Retorna um objeto Match se houver uma correspondência em qualquer parte da string.
split: Retorna uma lista onde a string foi dividida em cada correspondência.
sub: Substitui uma ou várias correspondências por uma string.


"""

# Módulo RegEx - Importe o remódulo:
import re

# Verifique se a string começa com "The" e termina com "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")


# A função findall():
# Imprima uma lista de todas as correspondências:


# Retorne uma lista contendo todas as ocorrências de "ai":
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# OBS: Se nenhuma correspondência for encontrada, uma lista vazia será retornada:
import re

txt = "The rain in Spain"

# Verifique se "Portugal" está na string:
x = re.findall("Portugal", txt)
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# A função search()
# Exemplo - Procure o primeiro caractere de espaço em branco na string:
import re

texto = "The rain in Spain"

resultado = re.search("\s", texto)  # Procura o primeiro espaço em branco na frase

# Mostra a posição onde foi encontrado o primeiro espaço
print("O primeiro caractere de espaço está na posição:", resultado.start())


# Exemplo - Faça uma pesquisa que não retorne nenhuma correspondência:
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)  # saída: none

# A função split()
# Exemplo - Dividir em cada caractere de espaço em branco:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)  # saída: ['The', 'rain', 'in', 'Spain']

# Você pode controlar o número de ocorrências especificando o maxsplit parâmetro:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)  # saída: ['The', 'rain in Spain']

# A função sub()
# Exemplo - Substitua cada caractere de espaço em branco pelo número 9:

import re

# A sub() substitui as correspondências pelo texto de sua escolha:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)  # saída: The9rain9in9Spain


# Você pode controlar o número de substituições especificando o count parâmetro:

import re

# Substitua as duas primeiras ocorrências de um caractere de espaço em branco pelo dígito 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)  # saída: The9rain9in Spain


# Match Object:
# Um objeto Match é um objeto que contém informações sobre a pesquisa e o resultado.
# Faça uma pesquisa que retornará um objeto Match:
import re

#A função search() retorna um objeto Match:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) # saída: <re.Match object; span=(5, 7), match='ai'>



