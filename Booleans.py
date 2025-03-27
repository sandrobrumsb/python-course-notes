#Booleans representam um de dois valores: True ou False.:
print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#A função bool() permite que você avalie qualquer valor e lhe dê True ou False em troca,
print(bool("Hello"))
print(bool(15))


"""
O Python também tem muitas funções integradas que retornam um valor booleano, como a isinstance() função ,
que pode ser usada para determinar se um objeto é de um determinado tipo de dados:
"""
x = 200
print(isinstance(x, int))