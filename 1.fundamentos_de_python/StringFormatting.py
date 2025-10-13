"""
Formatação de Strings em Python

Python oferece diversas formas de formatar textos, sendo as F-Strings (a partir do Python 3.6) a maneira mais moderna e recomendada.
Antes do Python 3.6, o método format() era o principal recurso para formatar strings.
Veja abaixo exemplos e dicas de como utilizar cada abordagem.
"""

txt = f"The price is 49 dollars"

###########################################################
# F-Strings
# Permite inserir variáveis, expressões e funções diretamente dentro de uma string.
# Basta colocar um 'f' antes das aspas da string.
###########################################################

texto = f"O preço é 49 reais"
print(texto)


# Exemplo - Adicione um espaço reservado para a variável preco:
preco = 59
texto = f"O preço é {preco} reais"
print(texto)


# Exibir o preço com 2 casas decimais:
preco = 59
texto = f"O preço é {preco:.2f} reais"
print(texto)

txt = f"The price is {95:.2f} dollars"

# Você também pode formatar um valor diretamente sem mantê-lo em uma variável:
texto = f"O preço é {95:.2f} reais"
print(texto)


# Executar operações em F-Strings:
texto = f"O preço é {20 * 59} reais"
print(texto)


# Você pode realizar operações matemáticas em variáveis:
preco = 59
taxa = 0.25
texto = f"O preço é {preco + (preco * taxa)} reais"
print(texto)


# Você pode executar instruções if...else dentro dos espaços reservados:
preco = 49
texto = f"Está {'Caro' if preco > 50 else 'Barato'}"
print(texto)


# Executar funções em F-Strings
# Exemplo - Use o método upper() para converter um valor em letras maiúsculas:
fruta = "maçã"
texto = f"Eu amo {fruta.upper()}"
print(texto)


# Você pode criar suas próprias funções e usá-las:
# Exemplo - Função que converte pés em metros:
def converter_para_metros(valor_pes):
    return valor_pes * 0.3048


texto = f"O avião está voando a {converter_para_metros(30000):.2f} metros de altitude"
print(texto)


# Existem vários outros modificadores que podem ser usados para formatar valores:
# Exemplo - Use uma vírgula como separador de milhar:
preco = 59000
texto = f"O preço é {preco:,} reais"
print(texto)


"""
Principais tipos de formatação para F-Strings:
:<     Alinha à esquerda
:>     Alinha à direita
:^     Centraliza
:,     Vírgula como separador de milhar
:_     Sublinhado como separador de milhar
:.2f   Duas casas decimais
:d     Decimal
:x     Hexadecimal minúsculo
:X     Hexadecimal maiúsculo
... e outros
"""


###########################################################
# Método format()
# Antes das F-Strings, o método format() era utilizado para inserir valores em strings.
###########################################################

preco = 49
texto = "O preço é {} reais"
print(texto.format(preco))


# Formate o preço para exibir duas casas decimais:
preco = 49
texto = "O preço é {:.2f} reais"
print(texto.format(preco))


# Vários valores
# Basta adicionar mais valores ao método format():
quantidade = 3
codigo_item = 567
preco = 49
pedido = "Quero {} unidades do item {} por {:.2f} reais."
print(pedido.format(quantidade, codigo_item, preco))


# Índices numéricos
# Use números dentro das chaves para garantir a ordem dos valores:
quantidade = 3
codigo_item = 567
preco = 49
pedido = "Quero {0} unidades do item {1} por {2:.2f} reais."
print(pedido.format(quantidade, codigo_item, preco))

age = 36
txt = "His name is {1}. {1} is {0} years old."

# Também é possível referenciar o mesmo valor mais de uma vez usando o índice:
idade = 36
nome = "João"
texto = "O nome dele é {1}. {1} tem {0} anos."
print(texto.format(idade, nome))


# Índices nomeados
# Use nomes dentro das chaves e passe os valores como argumentos nomeados:
pedido = "Eu tenho um {carro}, ele é um {modelo}."
print(pedido.format(carro="Ford", modelo="Mustang"))
