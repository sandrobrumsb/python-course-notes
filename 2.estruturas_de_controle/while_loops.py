# ---------------------------------------
# Python While.
# Python tem dois comandos de loop primitivos:
# - while loops
# - for loops
# ---------------------------------------

# Com o loop while, podemos executar um conjunto de instruções desde que uma condição seja verdadeira.
# Imprima i desde que i seja menor que 6:
i = 1
while i < 6:
    print(i)
    i += 1

# Sair do loop quando i for 3:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Com a instrução "continue" , podemos parar a iteração atual e continuar com a próxima:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)  ## Observe que o número 3 está faltando no resultado

# The else Statement - Com a instrução else, podemos executar um bloco de código uma vez quando a condição não for mais verdadeira,
# Imprima uma mensagem quando a condição for falsa:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i não é mais menor que 6")

# break Statement -
# Com a instrução break, podemos parar o loop mesmo se a condição while for verdadeira:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# continue Statement -
# Com a instrução continue , podemos parar a iteração atual e continuar com a próxima:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Observe que o número 3 está faltando no resultado

# else Statement -
# Com a instrução else, podemos executar um bloco de código uma vez quando a condição não for mais verdadeira:

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i não é mais menor que 6")


