# 1. Delete a File
# Para excluir um arquivo, você deve importar o módulo do sistema operacional e executar sua os.remove()função:
import os

os.remove("demofile.txt")

# 2. Verifique se o arquivo existe:
# Para evitar um erro, você pode verificar se o arquivo existe antes de tentar excluí-lo:
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# 3. Excluir pasta
# Para excluir uma pasta inteira, use o método os.rmdir():
import os

os.rmdir("myfolder")
