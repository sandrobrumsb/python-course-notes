# Declarando uma varianvel simples do tipo int e string:
x = 5
y = "Hello, World!"

## Variáveis ​​não precisam ser declaradas com nenhum tipo específico e podem até mesmo mudar de tipo depois de serem definidas.
x = 4      
x = "Sally" 
print(x)

##Se você quiser especificar o tipo de dados de uma variável, isso pode ser feito com conversão.
x = str(3)    # x vai ser uma string: '3'
y = int(3)    # y vai ser um inteiro:  3
z = float(3)  # z vai ser um float:    3.0
print(x) 
print(y)
print(z)

##Obter o tipo de dados de uma variável:
x = 5
y = "Ola"
print(type(x))
print(type(y))


meuNome = "Peter"            # nome de variavel em Camel Case.
MeuPrimeiroNome = "Peter"    # nome de variavel em Pascal Case.
meu_ultimo_nome = "Parker"   # nome de variavel em Snake Case.
print(meuNome,MeuPrimeiroNome,meu_ultimo_nome)

#Python permite que você atribua valores a várias variáveis ​​em uma linha:
x, y, z = "Orange", "Banana", "Cherry"
print(x,y,z)

# Um valor para múltiplas variáveis
x = y = z = "Orange"
print(x,y,z)

#Extraindo os valores de uma lista:
frutas = ['arroz','feijao','macarrao']
x,y,z = frutas
print(x)
print(y)
print(z)

## Você também pode usar o operador + para contatenar múltiplas variáveis:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

## Para números, o caractere + funciona como um operador matemático:
x = 5
y = 10
print(x + y)

## Para int com string NAO se usa o + somente se usa a virgula:
x = 5
y = "John"
print(x, y)

## Variáveis ​​Globais - que podem ser usadas dentro e fora da funções:
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

## Uma variável global, com o mesmo nome dentro de uma função, A variavel global permanecerá com o mesmo valor:
x = "GALO"

def myfunc():
  x = "fantastic"
  print("Python is " + x)   # uma variável dentro de uma função, essa variável é local e só pode ser usada dentro dessa função.

myfunc()

print("Python is " + x)

## Para criar uma variável global dentro de uma função, você pode usar a palavra-chave global.
def myfunc():
  global x
  x = "Galo"

myfunc()

print("Hexa cammpeao mineiro é " + x)

## Para alterar o valor de uma variável global dentro de uma função, consulte a variável usando a global + a variavel (x)
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)