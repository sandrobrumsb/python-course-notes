"""
Polimorfismo Python:
 - A palavra "polimorfismo" significa "muitas formas".
 - Em programação, refere-se a métodos/funções/operadores com o mesmo nome que podem ser executados em muitos objetos ou classes.
 - Um exemplo de uma função Python que pode ser usada em diferentes objetos é a função len().
 -
"""

# 1. Função de  Polimorfismo:
# Um exemplo de uma função Python que pode ser usada em diferentes objetos é a função len().


string = "Hello World!"

print(len(string))

tupla = ("apple", "banana", "cherry")

print(len(tupla))

dicionario = {"marca": "Ford", "modeloo": "Mustang", "year": 1964}

print(len(dicionario))


# 2. Polimorfismo de classe
# O polimorfismo é frequentemente usado em métodos de classe, onde podemos ter várias classes com o mesmo nome de método.
# Por exemplo, digamos que temos três classes: Carro, Barco, e Aviao,todas elas têm um método move():
# Exemplo - Classes diferentes com o mesmo método:
class Carrro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def move(self):
        print("Dirige!")


class Barco:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def move(self):
        print("Nada!")


class Aviao:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def move(self):
        print("Voa!")


carro1 = Carrro("Ford", "Mustang")  # Create a Car object
barco1 = Barco("Ibiza", "Touring 20")  # Create a Boat object
aviao1 = Aviao("AF", "71")  # Create a Plane object

for x in (carro1, barco1, aviao1):
    x.move()

# OBS: Observe o loop for no final. Graças ao polimorfismo, podemos executar o mesmo método para todas as três classes.

# 3. Polimorfismo de Classe de Herança
# Podemos usar polimorfismo com classes filhas com o mesmo nome
# Exemplo - Crie uma classe chamada Vehiclee faça Car, Boat, Plane classes filhas de Vehicle:


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("F", "70")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

# OBS: As classes filhas herdam as propriedades e métodos da classe pai,
# No exemplo acima, você pode ver que a Carclasse está vazia, mas herda brand, model, e move()de Vehicle.
# As classes Boat também herdam , e de , mas ambas substituem o método.Planebrandmodelmove()Vehiclemove()
