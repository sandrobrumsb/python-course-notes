# ---------------------------------------
# Python For.
# Um loop for é usado para iterar sobre uma sequência...
# pode ser uma lista, uma tupla, um dicionário, um conjunto ou uma string).:
# Com o loop for, podemos executar um conjunto de instruções, uma para cada item em uma lista, tupla conjunto etc.
# ---------------------------------------

# 1. EXEMPLO - Imprima cada fruta em uma lista de frutas:
fruits = ["apple", "banana", "cherry"]
for x in fruits:  # / PARA cada fruta em fruits, imprima (fruta)
    print(x)
# OBS: O loop for não requer uma variável de indexação definida previamente.

# 2. Looping através de uma string:
# Mesmo as strings são objetos iteráveis, elas contêm uma sequência de caracteres:
# EXEMPLO - Faça um loop pelas letras da palavra "banana":

for letra in "banana":  # PARA cada letra em banana, imprima letra
    print(letra)

# 3. break Statement:
# Com a instrução break, podemos parar o loop antes que ele tenha percorrido todos os itens:
# EXEMPLO - Sair do loop quando x for "banana":
frutas = ["apple", "banana", "cherry"]
for fruta in frutas:  # Para cada fruta em frutas, imprima fruta
    print(fruta)
    if fruta == "banana":  # Se fruta for igual a "banana", PARE.
        break

# EXEMPLO 2 - Sai do loop quando x for "banana", mas desta vez a BREAK vem antes da impressão:
frutas = ["apple", "banana", "cherry"]
for fruta in frutas:  # Para cada fruta em frutas,verifique...
    if fruta == "banana":  # Se fruta for igual a "banana", PARE.
        break
    print(fruta)  # print: Apple

# 4. Continue Statement - Com a instrução continue , podemos parar a iteração atual do loop e continuar com a próxima:
frutas = ["apple", "banana", "cherry"]
for x in frutas:  # Para cada elemento em frutas,verifique...
    if x == "banana":  # Se elemento for igual a "banana", CONTINUE...
        continue
    print(x)  # print: Apple Cherry

# 5. The range() Function:
# Para percorrer um conjunto em um número especifico de vezes, podemos usar a função range():
for x in range(6):
    print(x)  # print: 0 1 2 3 4 5

# Usando o parâmetro start:
for x in range(2, 6):
    print(x)  # print: 2 3 4 5

# Incremente a sequência de 3 em 3 numeros:
for x in range(2, 30, 3):
    print(x)  # print: 2 5 8 11 14 17 20 23 26 29

# 6. Else in For Loop:
# O else em um for especifica um bloco de código a ser executado quando o loop for concluído:

# EXEMPLO - Imprima todos os números de 0 a 5 e exiba uma mensagem quando o loop terminar:
for numero in range(6):  # Para cada numero em range(total de 6)
    print(numero)  # imrpima o numero, em seguida...
else:
    print("Finalmente terminou!")  # imprima a Frase!

# O else NÃO será executado se o loop for interrompido por uma breakinstrução.
# EXEMPLO 2 - Quebre o loop quando x for igual a 3:
for x in range(6):
    if x == 3:
        break  # Se o loop for interrompido, o bloco else não será executado complentamente.
    print(x)
else:
    print("Finalmente terminou!")  # print: 0 1 2

# 7. Loops aninhados: Um loop aninhado é um loop dentro de um loop.
# EXEMPLO - Escreva cada descrição para cada fruta:
descricao = ["Vermelho", "Grande", "Gostoso"]
fruta = ["Maçã", "Banana", "Morango"]

for x in descricao:  # para cada elemento em descricao
    for y in fruta:  # para cada elemento em fruta
        print(x, y)  # imprima: descrição + fruta

# 8. The pass Statement:
# Os for não podem estar vazios, mas se por algum motivo você tiver
# insira a instrução "pass" para evitar o erro.
for x in [0, 1, 2]:
    pass
# ter um loop for vazio como este geraria um erro sem a instrução pass
