"""
Funções lambda:

- Uma função lambda é uma pequena função anônima.
- Uma função lambda pode receber qualquer número de argumentos, mas só pode ter uma expressão.

Sintaxe:
lambda arguments : expression

"""

# 1. Exemplo: Adicione 10 ao argumento ae retorne o resultado:
# Cria uma função que recebe um valor 'a' e retorna 'a + 10'
func_lambda = lambda a: a + 10
# Chama a função com o valor 5. Aqui, 'a' vira 5 e o resultado será 5 + 10:
print(func_lambda(5))  # Vai imprimir 15

# 2. As funções lambda podem receber qualquer número de argumentos:
func_lambda = lambda a, b: a * b
print(func_lambda(5, 6))

func_lambda = lambda a, b, c: a + b + c
print(func_lambda(5, 6, 2))


# 3.- Por que usar funções Lambda?:
# é melhor quando você o usa como uma função anônima dentro de outra função
# Exemplo:
def minha_funcao(n):
    return lambda a: a * n


dobro = minha_funcao(2)
print(dobro(11))


# Ou use a mesma definição de função para criar uma função que sempre triplique o número que você enviar:
def minha_funcao(n):
    return lambda a: a * n


triplo = minha_funcao(3)
print(triplo(11))


# Ou use a mesma definição de função para criar ambas as funções, no mesmo programa:
def minha_funcao(n):
    return lambda a: a * n


dobro = minha_funcao(2)
triplo = minha_funcao(3)
print(dobro(11), triplo(11))

