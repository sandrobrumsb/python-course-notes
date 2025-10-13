"""
Python Try Except:

O try permite que você teste um  de código em busca de erros.

O except permite que você lide com o erro.

O else permite que você execute código quando não há erro.

O finally permite que você execute código, independentemente do resultado dos s try e except.

"""

# O try irá gerar uma exceção, porque x não está definido:
try:
    print(x)
except:
    print("Ocorreu uma exceção")

# OBS: 1. Como o bloco try gera um erro, o bloco except será executado.

# 1. Muitas exceções:
# Você pode definir quantos blocos de exceção quiser,
# Exemplo - Imprima uma mensagem se o bloco try gerar um erro NameErrore e para outros erros:
try:
    print(x)
except NameError:
    print("A variável x não está definida")
except:
    print("Outra coisa deu errado")

# Exemplo - Neste exemplo, o trybloco não gera nenhum erro:
# O bloco try não gera nenhum erro, então o bloco else é executado:
try:
    print("Hello")
except:
    print("Algo deu errado")
else:
    print("Nada deu errado")


# Finally:
# O bloco finally é executado independentemente se o bloco try gera algum erro ou não:

try:
    print(x)
except:
    print("Algo deu errado")
finally:
    print("O 'try except' está concluído")


# Exemplo - Tente abrir e gravar em um arquivo que não é gravável:
# O bloco try gerará um erro ao tentar gravar em um arquivo somente leitura:

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Algo deu errado ao gravar no arquivo")
    finally:
        f.close()
except:
    print("Algo deu errado ao abrir o arquivo")

# OBS: Algo deu errado ao abrir o arquivo

# Criar uma exceção:
# você pode escolher lançar uma exceção se uma condição ocorrer.
# Para lançar (ou levantar) uma exceção, use a raise
x = -1

if x < 0:
    raise Exception("Desculpe, não há números abaixo de zero")

# OBS: A raisepalavra-chave é usada para gerar uma exceção.
# Você pode definir que tipo de erro gerar e o texto a ser impresso para o usuário.

x = "OLA!"

if not type(x) is int:
  raise TypeError("Somente números inteiros são permitidos")

