"""
Iteradores Python:
- Iteradores em Python são objetos que permitem percorrer elementos de uma coleção, como listas, tuplas, dicionários, etc., um por um, sem precisar acessar os elementos pelo índice.
- Iterável: é qualquer objeto que pode ser "percorrido" (como listas, strings, tuplas...). Ele possui o método especial __iter__() que retorna um iterador.
- Iterador: é o objeto que realiza a iteração. Ele tem os métodos especiais:
 1. __iter__() → retorna o próprio iterador
 2.__next__() → retorna o próximo elemento da sequência. Quando não há mais elementos, levanta uma exceção StopIteration.

 - O método iter() que é usado para obter um iterador:

"""

# Exemplo:

lista = [1, 2, 3]
iterador = iter(lista)  # chama lista.__iter__()

print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3
print(next(iterador))  # StopIteration

# 1. Retorna um iterador de uma tupla e imprime cada valor:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Até mesmo strings são objetos iteráveis ​​e podem retornar um iterador:
# Strings também são objetos iteráveis, contendo uma sequência de caracteres:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# 2. Percorrendo um Iterador
# Também podemos usar um forloop para iterar por um objeto iterável:
# Exemplo - Iterar os valores de uma tupla:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

# Iterar os caracteres de uma string:
mystr = "banana"

for x in mystr:
    print(x)

# 3. Criar um Iterador
"""
Para criar um objeto/classe como um iterador, você precisa implementar os métodos __iter__()e __next__()para seu objeto.

- O método  __iter__() age de forma semelhante, você pode fazer operações (inicializar etc.), mas sempre deve retornar o próprio objeto iterador.

- O método __next__() também permite que você faça operações e deve retornar o próximo item na sequência.
"""
# Exemplo - Crie um iterador que retorne números, começando com 1, e cada sequência aumentará em um (retornando 1,2,3,4,5 etc.):


class MyNumbers:
    def __iter__(self):
        self.a = 1  # Inicializa a contagem
        return self

    def __next__(self):
        x = self.a  # Salva o valor atual
        self.a += 1  # Incrementa para a próxima chamada
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# 4. StopIteration -
# O exemplo acima continuaria para sempre se você tivesse instruções next() suficientes ou se ele fosse usado em um forloop.
# Para evitar que a iteração continue para sempre, podemos usar a StopIterationinstrução.
# No método __next__(), podemos adicionar uma condição de término para gerar um erro se a iteração for feita um número especificado de vezes:

# Exemplo - Parar após 20 iterações:


# Define uma classe chamada MyNumbers que será usada como um iterador
class MyNumbers:

    # Método especial __iter__ define o comportamento do iterador
    def __iter__(self):
        self.a = 1  # Inicializa a variável 'a' com 1; será o primeiro número retornado
        return self  # Retorna o próprio objeto, que agora é um iterador

    # Método especial __next__ define o que acontece a cada iteração
    def __next__(self):
        # Verifica se o valor atual de 'a' é menor ou igual a 20
        if self.a <= 20:
            x = self.a  # Salva o valor atual de 'a' em x
            self.a += 1  # Incrementa 'a' para a próxima chamada
            return x  # Retorna o valor salvo
        else:
            # Quando o limite é ultrapassado, levanta a exceção StopIteration
            # Isso sinaliza ao loop for que a iteração acabou
            raise StopIteration


# Cria uma instância da classe MyNumbers
myclass = MyNumbers()

# Usa a função iter() para obter um iterador do objeto myclass
myiter = iter(myclass)

# Loop for que consome os valores do iterador
# Internamente, o for chama next() até encontrar StopIteration
for x in myiter:
    print(x)  # Imprime cada número de 1 até 20
