# 1. read()método para ler o conteúdo do arquivo:
f = open("demofile.txt")
print(f.read())


# Se o arquivo estiver localizado em um local diferente, você terá que especificar o caminho do arquivo, assim:
f = open("D:\\myfiles\welcome.txt")
print(f.read())


# 2. Usando a declaração with.
# Você também pode usar a with ao abrir um arquivo:
with open("demofile.txt") as f:
    print(f.read())

# OBS: Então você não precisa se preocupar em fechar seus arquivos, a declaração with cuida disso.

# 3. Fechar arquivos
# É uma boa prática sempre fechar o arquivo quando terminar de usá-lo.
# Se você não estiver usando a with, deverá escrever uma instrução close para fechar o arquivo:
f = open("demofile.txt")
print(f.readline())
f.close()

# 4. Ler somente partes do arquivo
# Exemplo - Retorna os 5 primeiros caracteres do arquivo:
with open("demofile.txt") as f:
    print(f.read(5))


# 5. Ler linhas
# Você pode retornar uma linha usando o método readline():
# Exemplo - Leia uma linha do arquivo:
with open("demofile.txt") as f:
    print(f.readline())

# OBS-  Chamando readline()duas vezes, você pode ler as duas primeiras linhas:
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())


# Ao percorrer as linhas do arquivo, você pode ler o arquivo inteiro, linha por linha:

with open("demofile.txt") as f:
    for x in f:
        print(x)


