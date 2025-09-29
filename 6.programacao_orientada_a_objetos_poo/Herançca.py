"""
Herança Python:
- A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.
- Herança é um jeito de reaproveitar código, criando novas classes baseadas em classes existentes.
- Reutilização de código (evita repetição)
- Facilidade de manutenção e extensão
- Organização e estruturação lógica do programa
- A classe pai é a classe da qual se está herdando, também chamada de classe base.
- A classe filha é a classe que herda de outra classe, também chamada de classe derivada.

"""


# Exemplo básico:
class Animal:
    def falar(self):
        print("O animal faz um som.")


class Cachorro(Animal):  # Cachorro herda de Animal
    def falar(self):
        print("O cachorro late.")


a = Animal()
a.falar()  # Saída: O animal faz um som.

c = Cachorro()
c.falar()  # Saída: O cachorro late.


# 1. Criar uma classe pai.
# Exemplo - Crie uma classe chamada Person, com propriedades firstname e lastname , e um método:printname:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use a classe Person para criar um objeto e, em seguida, execute o método printname:
x = Person("John", "Doe")
x.printname()

# 2. Criar uma classe filha
"""
Para criar uma classe que herda a funcionalidade de outra classe, envie a classe pai como parâmetro ao criar a classe filha:
"""


# Exemplo - Crie uma classe chamada Student, que herdará as propriedades e métodos da classe Person:
class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()

# 3. Adicione a função __init__()
# Quando você define seu próprio __init__() na classe filha (Student), o Python não usa mais automaticamente o __init__() da classe pai (Person)


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(
            self, fname, lname
        )  # Você precisa chamar manualmente o construtor da classe pai.


x = Student("Mike", "Olsen")
x.printname()

# 4. Use a função super()
# super() chama o método da superclasse automaticamente, sem precisar usar o nome da classe pai diretamente.


# Definindo a classe base 'Person'
class Person:
    # Método construtor da classe 'Person', chamado automaticamente ao criar um novo objeto
    def __init__(self, fname, lname):
        self.firstname = fname  # Armazena o primeiro nome como atributo do objeto
        self.lastname = lname  # Armazena o sobrenome como atributo do objeto

    # Método que imprime o nome completo
    def printname(self):
        print(self.firstname, self.lastname)


# Definindo a classe 'Student' que herda da classe 'Person'
class Student(Person):
    # Método construtor da classe 'Student'
    def __init__(self, fname, lname):
        # Chama o construtor da superclasse (Person) para reutilizar o código de inicialização
        super().__init__(fname, lname)


# Criando um objeto da classe 'Student' com nome e sobrenome
x = Student("Mike", "Olsen")

# Chamando o método printname() do objeto x (herdado da classe 'Person')
x.printname()

# 5. Adicionar propriedades.
# Exemplo - Adicione uma propriedade chamada graduationyear a Studentclasse:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)


# 6.  Adicionar Métodos
# Adicione um método chamado welcome a classe Student:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()

