"""
Funções Python:

- Uma função é um bloco de código que só é executado quando é chamado.
- Você pode passar dados, conhecidos como parâmetros, para uma função.
- Uma função pode retornar dados como resultado.

"""


# 1. Criando uma função:
# Uma função é definida usando a  palavra-chave def:
def minha_funcao():
    print("Ola função")


minha_funcao()


# 2. Argumentos:
"""
# Informações podem ser passadas para funções como argumentos.
# Os argumentos são especificados após o nome da função, dentro dos parênteses.
# Você pode adicionar quantos argumentos quiser, basta separá-los com uma vírgula.
"""


def minha_funcao(argumento):
    print(argumento + " Este e um argumento")


minha_funcao("Ola")
minha_funcao("mundo")
minha_funcao("python")


# Parâmetros ou argumentos?
# Os termos parâmetro e argumento podem ser usados ​​para a mesma coisa:
# informações que são passadas para uma função.


# 3. Número de argumentos.
# EXEMPLO: Esta função espera 2 argumentos e recebe 2 argumentos:
def minha_funcao(arg1, arg2):
    print(arg1 + " " + arg2)


minha_funcao("Sandro", "Silva")


# Se você tentar chamar a função com 1 ou 3 argumentos, receberá um erro:
# Exemplo - Esta função espera 2 argumentos, mas recebe apenas 1:
def minha_funcao(arg1, arg2):
    print(arg1 + " " + arg2)


minha_funcao("Sandro")


# 4. Argumentos arbitrários, *args:
"""
# Se você não sabe quantos argumentos serão passados ​​para sua função,
# adicione * antes do nome do parâmetro na definição da função.
# Dessa forma, a função receberá uma tupla de argumentos e poderá acessar os itens adequadamente.
"""


# Exemplo - Se o número de argumentos for desconhecido, adicione um *antes do nome do parâmetro:
def familia(*kids):
    print("O filho mais novo e " + kids[2])  # posição 2 do conjunto = sasuke


familia("Naruto", "Sakura", "Sasuke")


# Argumentos de palavras-chave:
"""
# Você também pode enviar argumentos com a sintaxe chave = valor .
# Dessa forma, a ordem dos argumentos não importa.
# Exemplo:
# """


def familia(crianca1, crianca2, crianca3):
    print("O filho mais novo e " + crianca2)


familia(crianca1="Naruto", crianca2="Sakura", crianca3="Sasuke")


# Argumentos de palavras-chave arbitrárias, **kwargs:
"""
# Se você não sabe quantos argumentos de palavras-chave serão passados ​​para sua função,
# adicione dois asteriscos: ** antes do nome do parâmetro na definição da função.
# Dessa forma, a função receberá um dicionário de argumentos e poderá acessar os itens adequadamente:
"""


# Exemplo: Se o número de argumentos for desconhecido,
# adicione dois asteriscos  ** antes do nome do parâmetro:
def pessoa(**crianca):
    print("o sobre nome dele e " + crianca["sobre_nome"])


pessoa(primeiro_nome="Naruto", sobre_nome="Uzumaki")


# 5. Default Parameter Value.
# O exemplo a seguir mostra como usar um parâmetro default padrão.
# Se chamarmos a função sem argumento, ela usará o valor padrão:


def funcao(pais="Brasil"):
    print("Eu sou de " + pais)


funcao("Japao")
funcao("India")
funcao()  # Essa func recebe o valor atribuido no parametro (pais = "Brasil"), por esta vazia.
funcao("Russia")


# 6. Passando uma lista como argumento.
"""
# Você pode enviar qualquer tipo de dado de argumento para uma função,
# Ex: string, número, lista, dicionário etc...,
# e ele será tratado como o mesmo tipo de dado dentro da função.
# Por exemplo, se você enviar uma Lista como argumento, ela ainda será uma Lista quando chegar à função:
"""


def funcao(comida):
    for x in comida:
        print(x)


frutas = ["macã", "banana", "morango"]
# o resultado será: Sera impresso a listya de frutas, porque frutas[] = paremtro da função(comida).
funcao(frutas)  # print: maca banana morango


# 7. Retornando Valores.
# Para permitir que uma função retorne um valor, use a return instrução:


def funcao(x):
    return 5 * x


print(funcao(3))
print(funcao(5))
print(funcao(9))


# 8. A declaração de passe
"""
# As definições de função não podem estar vazias,
# mas se você tiver uma definição de função sem conteúdo,
# insira-a na instrução pass para evitar obter um erro:
"""


def myfunction():
    pass  # ter uma definição de função vazia como esta geraria um erro sem a instrução pass


# 9. Positional-Only Arguments:
"""
# Você pode especificar que uma função pode ter SOMENTE argumentos posicionais,
# ou SOMENTE argumentos de palavras-chave

# Para especificar que uma função pode ter apenas argumentos posicionais, 
# adicione , / após os argumentos:

/ (barra): Quando você coloca o caractere / após um argumento, isso indica que todos os argumentos antes dele devem ser passados somente como argumentos posicionais. Ou seja, você não pode passar esses argumentos usando o nome (por exemplo, não pode usar x=3).

Exemplo :
"""


def funcao(x, /):
    print(x)


funcao(3)

"""
Sem isso, , /você tem permissão para usar argumentos de palavras-chave, mesmo que a função espere argumentos posicionais...

Exemplo :
"""


def funcao(x):
    print(x)


funcao(x=3)

"""
Mas ao adicionar, , /você receberá um erro se tentar enviar um argumento de palavra-chave.

Exemplo :
"""


def funcao(x, /):
    print(x)


funcao(x=3)  # print: TypeError: my_function() got some positional-only...


# 10. Argumentos somente de palavras-chave:
"""
Para especificar que uma função pode ter apenas argumentos de palavras-chave, 
dicione *, antes dos argumentos.

Exemplo:
"""


def funcao(*, x):
    print(x)


funcao(x=3)


"""
Sem isso, *, você tem permissão para usar argumentos posicionais mesmo que a função espere argumentos de palavras-chave:

Exemplo:
"""


def funcao(x):
    print(x)


funcao(3)


# você receberá um erro se tentar enviar um argumento posicional:
def funcao(*, x):
    print(x)


funcao(3)

# 11. Combine somente posicional e somente palavra-chave:
"""
Você pode combinar os dois tipos de argumentos na mesma função.
você pode especificar como os argumentos devem ser passados para uma função utilizando os símbolos / e *.

Exemplo Prático:
"""


def funcao(a, b, /, *, c, d):
    print(a + b + c + d)


funcao(5, 6, c=7, d=8)

# 12. Recursão:
"""
1ª - O Python também aceita recursão de função, o que significa que uma função definida pode chamar a si mesma.
2ª - Isso tem a vantagem de permitir que você execute um loop pelos dados para chegar a um resultado.
3ª - O desenvolvedor deve ter muito cuidado com a recursão, pois pode ser muito fácil cair na armadilha de escrever uma função que nunca termina, ou que consome muita memória ou capacidade do processador.

Exemplo:

# A função começa com o número 6 e vai "descendo" até 0, fazendo chamadas recursivas.
# Quando chega em 0, começa a voltar e vai somando os números e imprimindo o resultado de cada soma à medida que vai voltando.
# O que acontece é que a função vai somando: 6 + 5 + 4 + 3 + 2 + 1, e cada vez que ela volta, ela mostra o valor da soma até aquele ponto.

Resultado da ida:
6 - soma_recursiva(6 - 1)
5 - soma_recursiva(5 - 1)
4 - soma_recursiva(4 - 1)
3 - soma_recursiva(3 - 1)
2 - soma_recursiva(2 - 1)
1 - soma_recursiva(1 - 1)
0 - Retorna 0 (caso base)

Resultado da soma:
Volta da chamada 1 + 0 = 1
Volta da chamada 2 + 1 = 3
Volta da chamada 3 + 2 + 1 = 6
Volta da chamada 4 + 3 + 2 + 1 = 10
Volta da chamada 5 + 4 + 3 + 2 + 1 = 15
Volta da chamada 6 + 5 + 4 + 3 + 2 + 1 = 21


"""


# Função recursiva para somar todos os números de k até 0
def soma_recursiva(k):
    # Se k for maior que 0, continua chamando a função para o próximo número menor
    if k > 0:
        # Chama a função de novo, diminuindo 1, até chegar em 0
        resultado = k + soma_recursiva(k - 1)
        # A cada volta mostra o resultado parcial da soma
        print(resultado)
    else:
        # Quando k chega a 0, para a recursão e retorna 0 (caso base)
        resultado = 0
    return resultado


# Exemplo de uso: vai somar 6 + 5 + 4 + 3 + 2 + 1 + 0
print("Resultado da soma:")
soma_recursiva(6)
