"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""
#Imprimindo o tipo de dados das variáve is:
a = str("Hello World")	
b = int(20)	
c = float(20.5)	
d = complex(1j)	
e = list(("apple", "banana", "cherry"))	
f = tuple(("apple", "banana", "cherry"))	
g = range(6)
h = dict(name="John", age=36)	
i = set(("apple", "banana", "cherry"))	
j = frozenset(("apple", "banana", "cherry"))	
k = bool(5)	
l = bytes(5)	
m = bytearray(5)	
n = memoryview(bytes(5))	

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(g,type(g))
print(h,type(h))
print(i,type(i))
print(j,type(j))
print(k,type(k))
print(l,type(l))
print(m,type(m))
print(n,type(n))

x = {"name" : "John", "age" : 36}
print(x,type(x))