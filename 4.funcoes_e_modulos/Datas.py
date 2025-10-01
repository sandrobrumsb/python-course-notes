"""
Datas Python:

Uma data em Python não é um tipo de dado próprio, mas podemos importar um módulo chamado datetime para trabalhar com datas como objetos de data.
"""

# Exemplo - Importe o módulo datetime e exiba a data atual:

import datetime

x = datetime.datetime.now()
print(x)

# Retorna o ano e o nome do dia da semana:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Criando objetos de data
# Para criar uma data, podemos usar a classe datetime(), (construtor) do datetime módulo.
# A datetime() requer três parâmetros para criar uma data: ano, mês e dia.
# Exemplo - Crie um objeto de data:
import datetime

x = datetime.datetime(1988, 11, 19)

print(x)

# OBS: A datetime() também aceita parâmetros para hora e fuso horário (hora, minuto, segundo, microssegundo, tzone),
# mas eles são opcionais e têm um valor padrão de 0, ( None para fuso horário).

# Método strftime()
# O datetimeobjeto tem um método para formatar objetos de data em strings legíveis.
# O método é chamado strftime() que recebe um parâmetro, "format", para especificar o formato da string retornada:
# Exemplo - Exibir o nome do mês:
import datetime

x = datetime.datetime(1988, 11, 19)

print(x.strftime("%B"))

"""
%a: Dia da semana, versão curta — Qua
%A: Dia da semana, versão completa — Quarta-feira
%w: Dia da semana como número de 0 a 6, sendo 0 para domingo — 3
%d: Dia do mês de 01 a 31 — 31
%b: Nome do mês, versão curta — Dez
%B: Nome do mês, versão completa — Dezembro
%m: Mês como número de 01 a 12 — 12
%y: Ano, versão curta, sem o século — 18
%Y: Ano, versão completa — 2018
%H: Hora de 00 a 23 — 17
%I: Hora de 00 a 12 — 05
%p: AM/PM — PM
%M: Minuto de 00 a 59 — 41
%S: Segundo de 00 a 59 — 08
%f: Microsegundo de 000000 a 999999 — 548513
%z: Deslocamento UTC — +0100
%Z: Fuso horário — CST
%j: Número do dia no ano de 001 a 366 — 365
%U: Número da semana no ano, com domingo como primeiro dia da semana, de 00 a 53 — 52
%W: Número da semana no ano, com segunda-feira como primeiro dia da semana, de 00 a 53 — 52
%c: Versão local de data e hora — Seg Dez 31 17:41:00 2018
%C: Século — 20
%x: Versão local da data — 31/12/18
%X: Versão local da hora — 17:41:00
%%: Caracter % — %
%G: Ano ISO 8601 — 2018
%u: Dia da semana ISO 8601 (1-7) — 1
%V: Número da semana ISO 8601 (01-53) — 01
"""
