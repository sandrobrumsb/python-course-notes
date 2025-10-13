"""
Entrada de Dados do Usuário em Python

Python permite que você obtenha informações diretamente do usuário durante a execução do programa, utilizando a função input().
Veja abaixo exemplos organizados e dicas de uso.
"""

# Entrada simples
# Solicite o nome do usuário e exiba uma saudação.

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")


# Entradas múltiplas
# Solicite várias informações do usuário e utilize-as em uma frase.

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
animal_favorito = input("Qual é seu animal favorito? ")
cor_favorita = input("Qual é sua cor favorita? ")
numero_favorito = input("Qual é seu número favorito? ")
print(
    f"Você gostaria de um(a) {animal_favorito} {cor_favorita} com {numero_favorito} patas?"
)

x = input("Enter a number:")


# Entrada numérica
# Para realizar cálculos, converta a entrada para número.

import math

numero = input("Digite um número: ")
raiz = math.sqrt(float(numero))
print(f"A raiz quadrada de {numero} é {raiz}")


# Validação de entrada
# Continue perguntando até o usuário digitar um número válido.

valido = False
while not valido:
    numero = input("Digite um número: ")
    try:
        numero = float(numero)
        valido = True
    except:
        print("Entrada inválida, tente novamente.")
print("Obrigado!")
