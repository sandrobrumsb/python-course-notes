"""
Existem três tipos numéricos em Python: int, float e complex:
"""

x = 1  # int
y = 2.8  # float
z = 1j  # complex
print(type(x))
print(type(y))
print(type(z))

"""
Int, ou inteiro, é um número inteiro, positivo ou negativo, sem decimais, de comprimento ilimitado:+

"""
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

"""
Float, ou "número de ponto flutuante", é um número, positivo ou negativo, que contém uma ou mais casas decimais.
Float também pode ser um número científico com um "e" para indicar a potência de 10.
"""
x = 1.10
y = 1.0
z = -35.59
a = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print(type(a))

"""
Em Python, complex é um tipo de dado nativo que representa números complexos
Você pode criar números complexos diretamente, utilizando a notação com j:
"""

x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

"""
Conversão de tipo: 
Você pode converter de um tipo para outro com os métodos
int(), float(), e complex():
"""

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
Número aleatório: O Python não tem uma função random() para criar um número aleatório, 
mas tem um módulo interno chamado random que pode ser usado para criar números aleatórios:
"""

import random

print(random.randrange(1, 100))
