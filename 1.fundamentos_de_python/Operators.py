"""
Operadores Aritméticos em Python:

+   Adição             x + y
-   Subtração          x - y
*   Multiplicação      x * y
/   Divisão            x / y
%   Módulo             x % y
**  Exponenciação      x ** y
//  Divisão inteira    x // y
"""

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5)
print(10 // 5)

"""
Operadores de Atribuição em Python:

=    Atribuição simples         x = 5
+=   Adição e atribuição        x += 3   (x = x + 3)
-=   Subtração e atribuição     x -= 3   (x = x - 3)
*=   Multiplicação e atribuição x *= 3   (x = x * 3)
/=   Divisão e atribuição       x /= 3   (x = x / 3)
%=   Módulo e atribuição        x %= 3   (x = x % 3)
//=  Divisão inteira e atribuição x //= 3 (x = x // 3)
**=  Exponenciação e atribuição x **= 3  (x = x ** 3)
&=   AND bit a bit e atribuição x &= 3   (x = x & 3)
|=   OR bit a bit e atribuição  x |= 3   (x = x | 3)
^=   XOR bit a bit e atribuição x ^= 3   (x = x ^ 3)
>>=  Deslocamento à direita     x >>= 3  (x = x >> 3)
<<=  Deslocamento à esquerda    x <<= 3  (x = x << 3)
:=   Atribuição em expressão    print(x := 3)
"""

x = 5
print(x)

# Operadores de comparação
print(5 != 3)

"""
Operadores Lógicos em Python:

and  Retorna True se ambas as condições forem verdadeiras      x < 5 and x < 10
or   Retorna True se pelo menos uma condição for verdadeira    x < 5 or x < 4
not  Inverte o resultado, retorna False se o resultado for True not(x < 5 and x < 10)
"""

x = 10
print(x > 3 or x < 4)

"""
Operadores de Identidade em Python:

is      Retorna True se ambas as variáveis forem o mesmo objeto      x is y
is not  Retorna True se ambas as variáveis não forem o mesmo objeto  x is not y
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   # True: z é o mesmo objeto que x
print(x is y)   # False: x e y têm o mesmo conteúdo, mas são objetos diferentes
print(x == y)   # True: x e y têm o mesmo conteúdo

"""
Operadores de Associação em Python:

Usados para testar se uma sequência está presente em um objeto.
"""

x = ["apple", "banana"]
print("banana" in x)

y = ["apple", "banana"]
print("pineapple" not in y)

"""
Operadores Bit a Bit (Binários):

&   AND bit a bit         x & y
|   OR bit a bit          x | y
^   XOR bit a bit         x ^ y
~   NOT bit a bit         ~x
<<  Deslocamento à esquerda x << 2
>>  Deslocamento à direita  x >> 2
"""

print(6 ^ 3)

"""
Precedência de Operadores:

1. Parênteses têm a maior precedência:
    Exemplo: (6 + 3) - (6 + 3)
"""
print((6 + 3) - (6 + 3))

"""
2. Multiplicação tem precedência maior que adição:
    Exemplo: 100 + 5 * 3
"""
print(100 + 5 * 3)

"""
Ordem de Precedência dos Operadores (do mais alto para o mais baixo):

()      Parênteses
**      Exponenciação
+x -x ~x  Unário: mais, menos, NOT bit a bit
* / // % Multiplicação, divisão, divisão inteira, módulo
+ -     Adição, subtração
<< >>   Deslocamento à esquerda/direita
&       AND bit a bit
^       XOR bit a bit
|       OR bit a bit
== != > >= < <= is is not in not in  Comparações, identidade, associação
not     NOT lógico
and     AND lógico
or      OR lógico
"""
