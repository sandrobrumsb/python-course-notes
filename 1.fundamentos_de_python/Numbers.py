"""
# Números em Python:

Tipos numéricos em Python:
- int (inteiro)
- float (ponto flutuante)
- complex (complexo)
"""

# Exemplos de tipos numéricos:
numero_inteiro = 1  # int
numero_float = 2.8  # float
numero_complexo = 1j  # complex

print(type(numero_inteiro))
print(type(numero_float))
print(type(numero_complexo))

# ----------------------------------------
# Tipo int (inteiro)
"""
Int, ou inteiro, é um número positivo ou negativo, sem casas decimais e de comprimento ilimitado.
"""

inteiro_1 = 1
inteiro_2 = 35656222554887711
inteiro_3 = -3255522

print(type(inteiro_1))
print(type(inteiro_2))
print(type(inteiro_3))

# ----------------------------------------
# Tipo float (ponto flutuante)
"""
Float, ou número de ponto flutuante, é um número positivo ou negativo que contém uma ou mais casas decimais.
Também pode ser um número científico, usando "e" para indicar a potência de 10.
"""

float_1 = 1.10
float_2 = 1.0
float_3 = -35.59
float_4 = -87.7e100

print(type(float_1))
print(type(float_2))
print(type(float_3))
print(type(float_4))

# ----------------------------------------
# Tipo complex (complexo)
"""
Complex é um tipo de dado nativo que representa números complexos.
Você pode criar números complexos diretamente utilizando a notação com 'j'.
"""

complexo_1 = 3 + 5j
complexo_2 = 5j
complexo_3 = -5j

print(type(complexo_1))
print(type(complexo_2))
print(type(complexo_3))

# ----------------------------------------
# Conversão de tipos numéricos
"""
Você pode converter entre tipos numéricos usando as funções:
- int()
- float()
- complex()
"""

valor_int = 1
valor_float = 2.8
valor_complex = 1j

# Converter de int para float:
convertido_float = float(valor_int)

# Converter de float para int:
convertido_int = int(valor_float)

# Converter de int para complex:
convertido_complex = complex(valor_int)

print(convertido_float)
print(convertido_int)
print(convertido_complex)

print(type(convertido_float))
print(type(convertido_int))
print(type(convertido_complex))

# ----------------------------------------
# Gerando números aleatórios
"""
O Python não possui uma função random() nativa, mas possui o módulo interno 'random' que pode ser usado para gerar números aleatórios.
"""

print(random.randrange(1, 100))
# Números em Python

"""
Existem três tipos numéricos em Python:
- int (inteiro)
- float (ponto flutuante)
- complex (complexo)
"""

# Exemplos de tipos numéricos:
x = 1  # int
y = 2.8  # float
z = 1j  # complex

print(type(x))
print(type(y))
print(type(z))

# -------------------------------
# Tipo int (inteiro)
"""
Int, ou inteiro, é um número positivo ou negativo, sem casas decimais e de comprimento ilimitado.
"""

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# -------------------------------
# Tipo float (ponto flutuante)
"""
Float, ou número de ponto flutuante, é um número positivo ou negativo que contém uma ou mais casas decimais.
Também pode ser um número científico, usando "e" para indicar a potência de 10.
"""

x = 1.10
y = 1.0
z = -35.59
a = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print(type(a))

# -------------------------------
# Tipo complex (complexo)
"""
Complex é um tipo de dado nativo que representa números complexos.
Você pode criar números complexos diretamente utilizando a notação com 'j'.
"""

x = 3 + 5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# -------------------------------
# Conversão de tipos numéricos
"""
Você pode converter entre tipos numéricos usando as funções:
- int()
- float()
- complex()
"""

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# Converter de int para float:
a = float(x)

# Converter de float para int:
b = int(y)

# Converter de int para complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# -------------------------------
# Gerando números aleatórios
"""
O Python não possui uma função random() nativa, mas possui o módulo interno 'random' que pode ser usado para gerar números aleatórios.
"""


print(random.randrange(1, 100))
"""
Existem três tipos numéricos em Python: int, float e complex:
"""
# Tipos Numéricos em Python:
# Existem três tipos principais:
# 1. int (inteiro)
# 2. float (ponto flutuante)
# 3. complex (complexo)
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
