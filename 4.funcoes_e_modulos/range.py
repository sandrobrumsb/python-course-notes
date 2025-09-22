"""
Intervalo Python:

A função interna range() retorna uma sequência imutável de números,
usada para executar um loop por um número específico de vezes.
Este conjunto de números tem seu próprio tipo de dado chamado range (Intervalo).

"""

# 1. Criando intervalos.
""" 
A função range() pode ser chamada com 1, 2 ou 3 argumentos, usando esta sintaxe:
range(start, stop, step)
"""
# Exemplo - Crie um intervalo de números de 0 a 9:

intervalo = range(10)
print(intervalo)
# convertendio para uma lista:
print(list(intervalo))

# 2. Usando dois argumentos.
intervalo = range(3, 10)
print(intervalo)
# convertendio para uma lista:
print(list(intervalo))

# 3. Usando tres argumentos.
# Se a função range for chamada com três argumentos, o terceiro argumento representa o stepvalor.

intervalo = range(3, 10, 2)
print(intervalo)
# convertendio para uma lista:
print(list(intervalo))

# 4. Usando intervalos
# Intervalos são frequentemente usados ​​em for,para iterar sobre uma sequência de números.

for intervalo in range(10):
    print(intervalo)

# 5. Usando lista para exibir intervalos.
# Exemplo - Converter intervalos  em listas diferentes:

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

# 6. Faixas de Ranges.
# Exemplo - Extraia uma subsequência de um intervalo:
faixa = range(10)
print(faixa[2])  # imprime o elemento de índice 2 da sequência.
print(faixa[:3])  # usando fatiamento (slicing): [:3] significa do início até o índice 3

# 7. Teste de Associação
# Os intervalos oferecem suporte a testes de associação com o o perador "in".
# Exemplo - Teste se os números 6 e 7 estão presentes em um intervalo:

# Cria um range que vai de 0 até 10 (exclusivo), pulando de 2 em 2
faixa = range(0, 10, 2)
print(list(faixa))  # Saída: [0, 2, 4, 6, 8]

print(6 in faixa)  # Saída: True, pois verifica se o número 6 está dentro do range.
print(7 in faixa)  # Saída: False, pois verifica se o número 7 está dentro do range.

# 8. Comprimento - Os intervalos oferecem suporte à função len() para obter o número de elementos no intervalo.
# Exemplo - Obtenha o comprimento de um intervalo:
faixa = range(0, 10, 2)
print(list(faixa))
print(len(faixa))  # cumpirmento da Range, saida = 5

