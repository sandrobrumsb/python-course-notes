"""
Matemática Python:
O Python tem um conjunto de funções matemáticas integradas, incluindo um extenso módulo matemático, que permite executar tarefas matemáticas em números.
"""

# Funções matemáticas integradas:
# As funções min()e max()podem ser usadas para encontrar o menor ou maior valor em um iterável:
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# A função abs() retorna o valor absoluto (positivo) do número especificado:
x = abs(-7.25)

print(x)

# A função retorna o valor de x elevado à potência de y (x y ).pow(x, y)
# Exemplo Retorna o valor de 4 elevado à potência de 3 (o mesmo que 4 * 4 * 4):

x = pow(4, 3)

print(x)


# O Módulo de Matemática.
# O Python também tem um módulo integrado chamado math, que amplia a lista de funções matemáticas.
# Para usá-lo, você deve importar o math(import math):
# Depois de importar o math, você pode começar a usar métodos e constantes do módulo.
# O math.sqrt(), por exemplo, retorna a raiz quadrada de um número:
import math

x = math.sqrt(64)

print(x)

# O math.ceil() arredonda um número para cima, para o inteiro mais próximo, e o math.floor() método arredonda um número para baixo, para o inteiro mais próximo, e retorna o resultado:
# Exemplo:
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)  # returns 2
print(y)  # returns 1

# A constante math.pi  retorna o valor de PI (3,14...):
import math

x = math.pi

print(x)
