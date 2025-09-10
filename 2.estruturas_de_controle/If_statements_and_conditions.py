"""
# ---------------------------------------
# Python suporta as condições lógicas usuais da matemática::
# ---------------------------------------

É igual a: a == b
Não é igual a: a != b
Menor que: a < b
Menor ou igual a: a <= b
Maior que: a > b
Maior ou igual a: a >= b

# Essas condições podem ser usadas de várias maneiras, mais comumente em "instruções if" e loops.

"""

# Declaração If:
a = 33
b = 200
if b > a:
    print("b e maior que a")


# Elif - é a maneira do Python dizer "se as condições anteriores não forem verdadeiras, então tente esta condição":

a = 33
b = 33
if b > a:
    print("b e maior que a")
elif a == b:
    print("a e b sao iguais")

# else - captura tudo que não é capturado pelas condições anteriores.
a = 200
b = 33
if b > a:
    print("b e maior que a")
elif a == b:
    print("a e b sao iguais")
else:
    print("a e maior que b")


# Você também pode ter um else sem o elif:
a = 200
b = 33
if b > a:
    print("b e maior que a")
else:
    print("b nao e maior que a")

# if em forma abreviada:
a = 200
b = 33
if a > b: 
    print("a e maior que b")

# Declaração if else de uma linha:
a = 2
b = 330
print("A") if a > b else print("B")

# Essa técnica é conhecida como Operadores Ternários ou Expressões Condicionais.
# Uma linha if else, com 3 condições:
numero_1 = 330
numero_2 = 330
print("A") if numero_1 > numero_2 else print("=") if numero_1 == numero_2 else print("B")


# And - A palavra-chave "and" é um operador lógico e é usada para combinar instruções condicionais.
# Teste se a for maior que b, E se c for maior que a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Ambas as condições são verdadeiras")

# Or - A palavra-chave "or" é um operador lógico e é usada para combinar instruções condicionais.
# Teste se a for maior que b, OU se a for maior que c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("Pelo menos uma das condições é verdadeira")

# Not - A palavra-chave "not" é um operador lógico e é usada para reverter o resultado da instrução condicional.
# Teste se a NÃO é maior que b:
a = 33
b = 200
if not a > b:
  print("a NÃO é maior que b")

# if Aninhado - Você pode ter instruções if dentro de instruções if, o que é chamado de instruções aninhadas:

x = 41
if x > 10:
  print("Acima de 10,")
  if x > 20:
    print("acima de 20!")
  else:
    print("não acima de 20.")

# A declaração de pass - as instruções if não podem estar vazias, 
# mas se por algum motivo você tiver uma instrução if sem conteúdo, 
# insira pass para evitar um erro:

a = 33
b = 200
if b > a:
  pass # sem a instrução pass, ter uma instrução if vazia como esta geraria um erro.

