# 1. Escrever em um arquivo existente
"""
Para gravar em um arquivo existente, você deve adicionar um parâmetro à open()função:

"a"- Acrescentar - será anexado ao final do arquivo
"w"- Escrever - substituirá qualquer conteúdo existente
"""
# Exemplo - Abra o arquivo "demofile.txt" e anexe o conteúdo ao arquivo:
with open("demofile.txt", "a") as f:
    f.write("Agora o arquivo tem mais conteúdo!")

# abra e leia o arquivo após o acréscimo:
with open("demofile.txt") as f:
    print(f.read())


# Substituir conteúdo existente
# Para substituir o conteúdo existente no arquivo, use o parâmetro w:
# Exemplo - Abra o arquivo "demofile.txt" e sobrescreva o conteúdo:
with open("demofile.txt", "w") as f:
    f.write("Ops! Apaguei o conteúdo!")

# abrir e ler o arquivo após a substituição:
with open("demofile.txt") as f:
    print(f.read())


# Criar um novo arquivo
"""
Para criar um novo arquivo em Python, use o open() , com um dos seguintes parâmetros:

"x"- Criar - criará um arquivo, retornará um erro se o arquivo existir
"a"- Acrescentar - criará um arquivo se o arquivo especificado não existir
"w"- Escrever - criará um arquivo se o arquivo especificado não existir

"""
# Exemplo - Crie um novo arquivo chamado "myfile.txt":

f = open("myfile.txt", "x")  # Resultado: um novo arquivo vazio é criado.
