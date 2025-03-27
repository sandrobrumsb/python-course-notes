"""
Strings em Python são cercadas por aspas simples ou duplas.
Você pode exibir uma string literal com a função print():
"""
print("Hello")
print('Hello')


# Citações dentro de citações:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Atribuir String a uma Variável:
a = "Hello"
print(a)



#Strings multilinha: Você pode atribuir uma string multilinha a uma variável usando três aspas.

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Ou três aspas simples:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings são matrizes:
#Pegue o caractere na posição 7 (lembre-se que o primeiro caractere tem a posição 0):
a = "Hello, World!"
print(a[7])

# Looping através de uma string: Faça um loop pelas letras da palavra "banana":

for x in "banana":
  print(x)

# A função len() retorna o comprimento de uma string:
a = "Hello, World!"
print(len(a))

# Verificar sequência de caracteres - Verifique se "free" está presente no texto a seguir:
txt = "The best things in life are free!"
print("free" in txt)

#Use-o em uma ifdeclaração:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

"""
Para verificar se uma determinada frase ou caractere NÃO está presente em uma string,
podemos usar a palavra-chave not in
"""
txt = "The best things in life are free!"
print("expensive" not in txt)

# IF: imprimir somente se "expensive" NÃO estiver presente:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# Fatiando Strings: Você pode retornar um intervalo de caracteres usando a sintaxe de fatia
b = "Hello, World!"
print(b[2:5])

# Fatiar desde o início:
b = "Hello, World!"
print(b[:5])

# Fatiar até o fim:
b = "Hello, World!"
print(b[2:])

#Indexação Negativa:
b = "Hello, World!"
print(b[-5:-2])

# O método upper() retorna a string em maiúsculas:
a = "Hello, World!"
print(a.upper())

# O método lower() retorna a string em minusculo:
a = "Hello, World!"
print(a.lower())

# O método strip() remove qualquer espaço em branco do início ou do fim:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# O método replace() substitui uma string por outra string:
a = "Hello, World!"
print(a.replace("H", "J"))

# O split()método retorna uma lista,
# onde o texto entre o separador especificado se torna os itens da lista:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Format - Strings:
#Para especificar uma string como uma f-string, basta colocar um f na frente,
# dicionar chaves {} para espaços reservados para variáveis ​​e outras operações.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

"""
Um modificador é incluído adicionando dois pontos : ,
seguidos de um tipo de formataçã como .2f o que significa número de ponto fixo com 2 decimais:
"""
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Um espaço reservado pode conter código Python, como operações matemáticas:
txt = f"The price is {20 * 59} dollars"
print(txt)


# O caractere de escape permite que você use aspas duplas quando normalmente não seria permitido:
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 



