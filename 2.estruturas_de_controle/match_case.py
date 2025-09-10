# ---------------------------------------
# A instrução match é usada para executar diferentes ações com base em diferentes condições.
# ---------------------------------------


# 1. A instrução match seleciona um dos muitos blocos de código a serem executados:
# sixtase:

"""
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

"""

# O exemplo abaixo usa o número do dia da semana para imprimir o nome do dia da semana:
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


# 2. Default Value:
# Use o caractere " _ " como o último valor do caso,
# se quiser que um bloco de código seja executado,
# quando não houver outras correspondências:
day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")


# Combinar Valores - Use o caractere de barra vertical | como um operador
# ou na "avaliação de case" para verificar se há mais de um valor correspondente em um case

day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

# Você pode adicionar declarações if na avaliação do caso,
# como uma verificação de condição extra:
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
